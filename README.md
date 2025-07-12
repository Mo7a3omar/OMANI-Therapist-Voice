# OMANI-Therapist-Voice: AI Mental Health Assistant

## 🚨 Important Disclaimer

**⚠️ This project is a research prototype and is NOT intended for clinical use.**

This application is:
- **Not scientifically validated** for therapeutic effectiveness
- **Not a substitute** for professional mental health treatment
- **Requires significant additional research** and clinical validation
- **Needs collaboration** with licensed mental health professionals, cultural experts, and Arabic language specialists
- **Should not be used** for actual crisis intervention without proper professional oversight

**For mental health emergencies, please contact:**
- Emergency Services: 999 (Oman)
- Mental Health Support: +968-2205-5555
- Crisis Hotline: +968-2205-6666

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Testing Framework](#testing-framework)
- [Project Structure](#project-structure)
- [Technical Requirements](#technical-requirements)
- [Cultural Considerations](#cultural-considerations)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Future Work](#future-work)
- [License](#license)

## ✨ Features

### Core Functionality
- **Real-time voice interaction** in Omani Arabic dialect
- **Speech-to-Text (STT)** processing for Arabic audio input
- **AI-powered responses** using Google Gemini models
- **Text-to-Speech (TTS)** output in natural Arabic voice
- **Crisis detection** with emergency protocol activation
- **Cultural adaptation** for Omani and Gulf contexts

### Technical Features
- **Dual-model architecture** (Gemini Pro/Flash for optimal performance)
- **Sub-20 second response latency** for natural conversation flow
- **Session management** with conversation history
- **Performance monitoring** and metrics collection
- **Comprehensive testing suite** for validation

### Cultural Integration
- **Authentic Omani expressions** and dialectal terms
- **Islamic values integration** in therapeutic approaches
- **Family-centered counseling** approaches
- **Gender-appropriate** communication styles
- **Religious/spiritual** counseling integration when appropriate

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Voice Input   │───▶│  Speech-to-Text  │───▶│ Intent Analysis │
│   (Microphone)  │    │   (Arabic STT)   │    │ & Crisis Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Voice Output   │◀───│  Text-to-Speech  │◀───│ Gemini AI Model │
│   (Speakers)    │    │   (Arabic TTS)   │    │ (Pro/Flash)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                       ┌──────────────────┐    ┌─────────────────┐
                       │ Cultural Validator│◀───│ Response Filter │
                       │ & Safety Check   │    │ & Enhancement   │
                       └──────────────────┘    └─────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Microphone and speakers/headphones

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/omani-therapist-voice.git
   cd omani-therapist-voice
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   Create a `.streamlit/secrets.toml` file:
   ```toml
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 💻 Usage

### Basic Operation
1. **Launch the application** using the command above
2. **Click the microphone button** to start recording
3. **Speak clearly in Omani Arabic**
4. **Click again to stop recording**
5. **Listen to the AI's response** which plays automatically

### Supported Conversation Types
- General anxiety and stress management
- Family relationship counseling
- Work-related stress discussions
- Religious and spiritual guidance
- Crisis intervention (with appropriate disclaimers)

### Example Interactions
```
User: "أنا قلقان وايد من الشغل، ما أقدر أرقد الليل"
(I'm very anxious about work, I can't sleep at night)




## Testing Framework

The project includes a comprehensive testing framework to evaluate:

- **Performance:** Measures latency of speech-to-text, AI response, and text-to-speech components
- **Cultural Validation:** Ensures AI responses use authentic Omani expressions and respect cultural sensitivities
- **Crisis Detection:** Tests the accuracy of identifying crisis-related utterances
- **Load and Stress Testing:** Simulates multiple concurrent users to assess system scalability and robustness

### Running Tests

```bash
# Run performance tests
python performance_tester.py

# Run cultural validation
python cultural_validator.py

# Run crisis detection tests
python crisis_detector.py

# Run load and stress tests
python load_tester.py
```

## 📁 Project Structure

```
omani-therapist-voice/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── test_cases_omani.py             # Authentic Omani Arabic test cases
├── performance_tester.py           # Performance testing framework
├── cultural_validator.py           # Cultural appropriateness testing
├── crisis_detector.py              # Crisis detection testing
├── load_tester.py                  # Load and stress testing utilities
└── README.md                      # Project documentation
```

## 🔧 Technical Requirements

### System Requirements
- Python 3.8 or higher
- Internet connection for API access
- Microphone and speakers/headphones
- 4GB RAM minimum (8GB recommended)
- Modern web browser with microphone permissions

### API Dependencies
- Google Gemini API access
- Google Speech-to-Text API (optional, for enhanced accuracy)
- Google Text-to-Speech API (optional, for better voice quality)

### Python Dependencies
All required packages are listed in `requirements.txt`:
- streamlit>=1.30.0
- google-generativeai>=0.3.0
- gTTS>=2.3.0
- SpeechRecognition>=3.10.0
- pydub>=0.25.1
- st-audiorec>=0.1.2

## 🏛️ Cultural Considerations

### Omani Arabic Integration
- Uses authentic Omani dialect expressions like "شلونك" (How are you?), "ما عليك" (Don't worry), "بإذن الله" (God willing)
- Incorporates Gulf-specific cultural nuances and social dynamics
- Respects traditional family structures and gender-appropriate communication

### Islamic Values Integration
- Incorporates Islamic counseling principles when contextually appropriate
- Includes spiritual coping mechanisms like prayer (دعاء) and trust in Allah (توكل)
- Respects religious sensitivities and avoids culturally inappropriate advice

### Therapeutic Approach
- Adapts Cognitive Behavioral Therapy (CBT) techniques for Arabic-speaking populations
- Emphasizes family and community support systems
- Integrates traditional healing practices with modern therapeutic methods

## ⚠️ Limitations

### Technical Limitations
- Speech recognition accuracy varies with audio quality and background noise
- Response latency depends on internet connection and API availability
- Limited to text-based AI responses without visual or multimedia support

### Clinical Limitations
- **Not clinically validated** - requires extensive testing with mental health professionals
- **Cannot replace human therapists** - lacks the nuanced understanding of licensed professionals
- **Crisis detection is keyword-based** - may miss subtle indicators or cultural expressions of distress
- **No persistent memory** - cannot track long-term therapeutic progress

### Cultural Limitations
- Primarily designed for Omani dialect - may not fully capture other Gulf variations
- Requires validation by native speakers and cultural experts
- May not address all cultural subgroups within Omani society

## 🤝 Contributing

We welcome contributions from:

### Mental Health Professionals
- Clinical psychologists and psychiatrists
- Licensed counselors and therapists
- Crisis intervention specialists
- Cultural therapy experts

### Technical Contributors
- Arabic NLP researchers
- Speech recognition specialists
- AI/ML engineers
- Mobile and web developers

### Cultural Experts
- Native Omani Arabic speakers
- Islamic counseling specialists
- Gulf culture researchers
- Community leaders and social workers

### How to Contribute
1. **Open Issues** for bugs, feature requests, or cultural concerns
2. **Submit Pull Requests** with clear descriptions and testing
3. **Provide Feedback** on cultural appropriateness and therapeutic effectiveness
4. **Share Research** and validation studies

## 🔮 Future Work

### Short-term Goals (3-6 months)
- **Clinical Validation:** Partner with Omani healthcare institutions for testing
- **Enhanced Crisis Detection:** Implement advanced NLP for better safety protocols
- **Voice Quality Improvement:** Integrate higher-quality Arabic TTS systems
- **Mobile Application:** Develop native iOS/Android apps for better accessibility

### Medium-term Goals (6-12 months)
- **Professional Oversight:** Integrate licensed therapist supervision features
- **Expanded Dialects:** Support for other Gulf Arabic variants (UAE, Kuwait, Qatar)
- **Therapeutic Modules:** Specialized programs for anxiety, depression, PTSD
- **Family Therapy Features:** Multi-user sessions for family counseling

### Long-term Vision (1-3 years)
- **Clinical Trials:** Conduct randomized controlled trials for efficacy
- **Healthcare Integration:** Partner with Omani Ministry of Health
- **AI Advancement:** Develop specialized Arabic mental health language models
- **Regional Expansion:** Extend to other Arabic-speaking countries with cultural adaptations

### Research Priorities
- Validate therapeutic effectiveness through peer-reviewed studies
- Develop culturally-adapted mental health assessment tools
- Create training datasets for Arabic mental health NLP
- Establish ethical guidelines for AI-based mental health support in Arab cultures

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ License and copyright notice required
- ❗ No warranty provided

## 🚨 Final Disclaimer

**This project is experimental and intended for research and educational purposes only.**

### Important Reminders
- **Not a replacement** for professional mental health services
- **Requires clinical validation** before any therapeutic use
- **Should be supervised** by licensed mental health professionals
- **May not be suitable** for individuals in acute mental health crises

### Emergency Resources
If you or someone you know is in crisis, please seek immediate help:

**Oman Emergency Services:**
- Emergency: 999
- Mental Health Support: +968-2205-5555
- Crisis Hotline: +968-2205-6666

**International Resources:**
- International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/
- Crisis Text Line: Text HOME to 741741
