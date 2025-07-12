import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import speech_recognition as sr
from st_audiorec import st_audiorec
import io
import logging
import base64

# --- Configuration and Setup ---

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(
    page_title="المساعد النفسي العماني",
    page_icon="🧠",
    layout="centered"
)

# Function to automatically play audio
def autoplay_audio(audio_bytes: bytes):
    """Encodes audio bytes to base64 and uses HTML to autoplay it."""
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true" style="display:none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# Configure Gemini API Key
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')
    logger.info("Gemini API configured successfully.")
except (KeyError, Exception) as e:
    st.error("🛑 **خطأ فادح:** مفتاح واجهة برمجة تطبيقات Gemini غير مهيأ.")
    logger.error(f"Gemini API key error: {e}")
    st.stop()

# --- Core Helper Functions ---

def transcribe_audio(wav_audio_data):
    """Converts WAV audio bytes to text using Google's speech recognition."""
    recognizer = sr.Recognizer()
    try:
        audio_file = io.BytesIO(wav_audio_data)
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        
        text = recognizer.recognize_google(audio_data, language="ar-OM")
        logger.info(f"Transcribed: '{text}'")
        return text
    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
        return None
    except sr.RequestError as e:
        logger.error(f"Speech recognition error: {e}")
        return None

def get_gemini_response(user_input: str, conversation_history: list):
    """Generates therapeutic response using Gemini model with enhanced therapist behavior."""
    
    # Crisis detection with immediate intervention
    crisis_keywords = ["انتحار", "أموت", "أنهي حياتي", "ما فيني أعيش", "تعبت من الحياة", "ما عاد فيني"]
    if any(keyword in user_input for keyword in crisis_keywords):
        logger.warning("Crisis detected")
        return """
        أسمع أنك تمر بوقت صعب جداً، وأريدك تعرف إني هنا معاك. سلامتك أهم شيء في الدنيا.
        
        أرجوك تواصل فوراً مع:
        📞 خط الطوارئ: 999
        📞 خط الدعم النفسي: +968-2205-5555
        📞 خط الأمل: +968-2205-6666
        
        حياتك ثمينة وايد، وفي ناس كثير يقدرون يساعدونك الحين. ما تتردد تطلب المساعدة.
        """, "crisis"

    # Enhanced therapeutic system prompt
    system_prompt = """
    أنت معالج نفسي محترف ومتخصص في اللهجة العمانية والثقافة الخليجية. أنت تتحدث مع شخص يحتاج للدعم النفسي.

    كمعالج محترف، يجب أن تكون:
    
    🎯 **المهارات العلاجية:**
    - استخدم تقنيات الاستماع النشط والتعاطف
    - اطرح أسئلة مفتوحة لفهم المشاعر بعمق
    - استخدم تقنيات العلاج المعرفي السلوكي المناسبة ثقافياً
    - قدم استراتيجيات عملية للتأقلم والتحسن
    - اعكس المشاعر وأعد صياغتها لإظهار الفهم
    
    🏛️ **الحساسية الثقافية:**
    - استخدم تعبيرات عمانية أصيلة (شلونك، ما عليك، بإذن الله، يلا نشوف)
    - احترم القيم الإسلامية والعائلية العمانية
    - ادمج الممارسات الروحية عند المناسبة (الدعاء، التوكل على الله)
    - تفهم ديناميكيات الأسرة الخليجية والضغوط الاجتماعية
    
    💬 **أسلوب التواصل:**
    - كن دافئاً ومتعاطفاً ومطمئناً
    - استخدم نبرة هادئة وداعمة
    - اجعل الردود قصيرة ومركزة (2-4 جمل)
    - اطرح سؤال واحد في نهاية كل رد لتشجيع المحادثة
    
    ❌ **تجنب تماماً:**
    - التشخيصات الطبية أو وصف الأدوية
    - إعطاء نصائح مباشرة دون فهم السياق
    - التقليل من مشاعر الشخص أو الحكم عليها
    - الردود الطويلة أو المعقدة
    - استبدال العلاج النفسي المهني
    
    🎭 **أمثلة على الردود العلاجية:**
    - "أفهم إنك تحس بـ... هذا صعب عليك. شنو أكثر شي يخليك تحس كذا؟"
    - "شلونك اليوم؟ أحس إن فيك شي يضايقك... تبي تحكيلي عنه؟"
    - "ما عليك، كلنا نمر بأوقات صعبة. أنت مو لحالك في هذا الشي."
    - "بإذن الله راح نشتغل سوا عشان تحس أحسن. شنو رأيك نجرب...؟"
    
    تذكر: أنت معالج محترف يساعد شخص يثق فيك. كن حاضراً معه بكل تعاطف ومهنية.
    """
    
    # Build comprehensive prompt with conversation context
    full_prompt = f"{system_prompt}\n\n"
    
    # Add recent conversation history for context
    if conversation_history:
        full_prompt += "سياق المحادثة السابقة:\n"
        for entry in conversation_history[-3:]:  # Last 3 exchanges
            full_prompt += f"المستخدم: {entry['user']}\nالمعالج: {entry['assistant']}\n"
        full_prompt += "\n"
    
    # Add current user input
    full_prompt += f"المستخدم الآن يقول: {user_input}\n\n"
    full_prompt += "رد عليه كمعالج نفسي محترف باللهجة العمانية، مع طرح سؤال مناسب لمواصلة العلاج:\nالمعالج:"

    try:
        # Generate response with therapeutic parameters
        response = gemini_model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,  # Balanced creativity and consistency
                top_p=0.8,
                top_k=40,
                max_output_tokens=200,  # Keep responses concise
            )
        )
        logger.info("Therapeutic response generated successfully")
        return response.text, "normal"
    except Exception as e:
        logger.error(f"Gemini error: {e}")
        return "عذراً، حدث خطأ تقني. بس أنا هنا معاك، حاول مرة أخرى وحكيلي شنو في بالك.", "error"

def text_to_speech(text: str):
    """Converts text to speech using gTTS."""
    try:
        tts = gTTS(text=text, lang='ar', slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        logger.info("TTS conversion successful")
        return audio_fp.read()
    except Exception as e:
        logger.error(f"TTS error: {e}")
        return None

# --- Main UI Layout ---

# Header
st.title("🧠 المساعد النفسي العماني")
st.write("مساحة آمنة للتحدث... اضغط على المايكروفون وتحدث")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'processing' not in st.session_state:
    st.session_state.processing = False

# --- Recording Section ---
st.subheader("🎤 اضغط للتسجيل")

# Audio recorder widget
wav_audio_data = st_audiorec()

# --- Processing Logic ---
if wav_audio_data and not st.session_state.processing:
    st.session_state.processing = True
    
    # Show processing message
    with st.spinner("🎧 جاري الاستماع والتفكير..."):
        
        # Step 1: Transcribe audio
        user_text = transcribe_audio(wav_audio_data)
        
        if user_text:
            # Display user message
            st.write(f"**👤 أنت:** {user_text}")
            
            # Step 2: Get AI response
            ai_text, response_type = get_gemini_response(user_text, st.session_state.history)
            
            if ai_text:
                # Display AI message
                if response_type == "crisis":
                    st.error(f"**🚨 المعالج:** {ai_text}")
                else:
                    st.success(f"**🧠 المعالج:** {ai_text}")
                
                # Step 3: Convert to speech and play automatically
                ai_audio = text_to_speech(ai_text)
                if ai_audio:
                    autoplay_audio(ai_audio)
                    st.info("🔊 جاري تشغيل الرد...")
                
                # Add to conversation history
                st.session_state.history.append({
                    "user": user_text, 
                    "assistant": ai_text,
                    "type": response_type
                })
        else:
            st.warning("⚠️ لم أتمكن من فهم الصوت. حاول مرة أخرى بصوت أوضح.")
    
    st.session_state.processing = False

# --- Optional Conversation History ---
if st.session_state.history:
    with st.expander("📜 عرض سجل المحادثة", expanded=False):
        for i, entry in enumerate(reversed(st.session_state.history[-5:])):
            st.write(f"**👤 أنت:** {entry['user']}")
            st.write(f"**🧠 المعالج:** {entry['assistant']}")
            if i < len(st.session_state.history) - 1:
                st.divider()

# --- Minimal Sidebar ---
with st.sidebar:
    st.header("📝 كيفية الاستخدام")
    st.write("""
    1. **اضغط على المايكروفون** 🎤
    2. **تحدث بوضوح** 🗣️
    3. **اضغط مرة أخرى لإيقاف التسجيل** ⏹️
    4. **استمع للرد التلقائي** 🔊
    """)
    
    st.divider()
    
    # Clear conversation button
    if st.button("🗑️ مسح المحادثة"):
        st.session_state.history = []
        st.rerun()
    
    st.divider()
    
    # Safety disclaimer
    st.warning("""
    ⚠️ **تنبيه مهم**
    
    هذا النظام للمساعدة فقط ولا يغني عن استشارة الطبيب النفسي المختص.
    
    في حالات الطوارئ، اتصل بـ:
    - الطوارئ: 999
    - الدعم النفسي: +968-2205-5555
    """)

# --- Footer ---
st.divider()
st.caption("تم تطوير هذا النظام لتقديم الدعم النفسي الأولي باللهجة العمانية")
