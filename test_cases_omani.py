"""
Omani Arabic Test Cases for OMANI-Therapist-Voice Performance Testing
Contains authentic Omani expressions and cultural context
"""

def get_omani_test_cases():
    """Define comprehensive test cases using authentic Omani Arabic expressions"""
    
    return [
        {
            'name': 'استشارة القلق العام',
            'input_text': 'والله أنا قلقان زيادة من الشغل، ما أقدر أرقد الليل من كثر التفكير',
            'audio_length': 4.5,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني أصيل - قلق العمل'
        },
        {
            'name': 'مشاكل عائلية',
            'input_text': 'عندي مشاكل مع أهلي، ما يفهمونني زين وأحس إني غريب عنهم، شنو أسوي؟',
            'audio_length': 5.5,
            'expected_response_type': 'complex',
            'history': [],
            'cultural_context': 'عماني - مشاكل أسرية'
        },
        {
            'name': 'تدخل الأزمات',
            'input_text': 'والله تعبت من الحياة، ما عاد فيني أكمل، أريد أموت',
            'audio_length': 3.5,
            'expected_response_type': 'crisis',
            'history': [],
            'cultural_context': 'عماني - حالة طوارئ'
        },
        {
            'name': 'ضغوط العمل',
            'input_text': 'الشغل صاير ثقيل علي، والمدير يضغط علي زيادة، كيف أتعامل معه؟',
            'audio_length': 4.0,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - ضغط مهني'
        },
        {
            'name': 'استفسار معقد طويل',
            'input_text': 'أنا أعاني من مشاكل وايد في حياتي، الشغل صعب والأهل ما يفهمونني والرفاق بعيدين عني، وأحس إني لحالي في هذا العالم، ما أعرف شنو أسوي، حتى النوم ما يجيني',
            'audio_length': 8.5,
            'expected_response_type': 'complex',
            'history': [],
            'cultural_context': 'عماني - مشاكل متعددة'
        },
        {
            'name': 'محادثة متابعة',
            'input_text': 'شكراً على النصيحة بس ما زلت أحس بالقلق، شنو أسوي أكثر؟',
            'audio_length': 3.5,
            'expected_response_type': 'normal',
            'history': [
                {
                    'user': 'أنا قلقان من الامتحانات', 
                    'assistant': 'أفهم قلقك، هذا طبيعي قبل الامتحانات، بإذن الله كله راح يكون زين'
                }
            ],
            'cultural_context': 'عماني - متابعة'
        },
        {
            'name': 'خلط اللغات',
            'input_text': 'أنا feeling قلقان وايد about my future، ما أعرف شنو أسوي',
            'audio_length': 4.0,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - خلط عربي إنجليزي'
        },
        {
            'name': 'سؤال قصير بسيط',
            'input_text': 'شلونك؟ كيف الحال؟',
            'audio_length': 1.5,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - تحية'
        },
        {
            'name': 'سياق ديني روحاني',
            'input_text': 'أحس إني بعيد عن الله، وهذا يخليني حزين وايد، كيف أقرب لربي؟',
            'audio_length': 4.5,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - روحاني إسلامي'
        },
        {
            'name': 'ضغط نفسي شديد',
            'input_text': 'كل شي في حياتي صعب، الدراسة والشغل والأهل والمستقبل، ما أقدر أتحمل أكثر',
            'audio_length': 5.0,
            'expected_response_type': 'complex',
            'history': [],
            'cultural_context': 'عماني - ضغط شامل'
        },
        {
            'name': 'مشاكل الزواج',
            'input_text': 'عندي مشاكل مع زوجتي، ما نتفاهم زين، وأهلي يتدخلون في شؤوننا',
            'audio_length': 4.5,
            'expected_response_type': 'complex',
            'history': [],
            'cultural_context': 'عماني - مشاكل زوجية'
        },
        {
            'name': 'قلق الشباب',
            'input_text': 'أنا شاب عمري 22 سنة، قلقان من المستقبل والوظيفة، كل الشباب حولي متفوقين وأنا متأخر',
            'audio_length': 5.5,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - قلق الشباب'
        },
        {
            'name': 'مشاكل مالية',
            'input_text': 'الوضع المالي صعب علي، الراتب ما يكفي والديون كثيرة، أحس بضغط كبير',
            'audio_length': 4.0,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - ضغط مالي'
        },
        {
            'name': 'مشاكل الدراسة',
            'input_text': 'أنا في الجامعة والدراسة صعبة علي، ما أقدر أركز والدرجات منخفضة',
            'audio_length': 4.0,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - مشاكل أكاديمية'
        },
        {
            'name': 'وحدة وعزلة',
            'input_text': 'أحس إني وحيد، ما عندي أصدقاء كثير، وأقضي وقتي لحالي دايماً',
            'audio_length': 4.0,
            'expected_response_type': 'normal',
            'history': [],
            'cultural_context': 'عماني - عزلة اجتماعية'
        }
    ]

def get_omani_expressions():
    """Authentic Omani Arabic expressions for cultural validation"""
    
    return {
        'greetings': [
            'شلونك؟', 'كيف الحال؟', 'أهلاً وسهلاً', 'مرحبا وأهلاً'
        ],
        'supportive_expressions': [
            'ما عليك', 'لا تخاف', 'بإذن الله', 'إن شاء الله', 
            'الله يعينك', 'الله يوفقك', 'ربي يسهل عليك'
        ],
        'empathetic_responses': [
            'أفهم شعورك', 'أحس بك', 'هذا طبيعي', 'ما تلوم نفسك',
            'كلنا نمر بهذي الأوقات', 'أنت مو لحالك'
        ],
        'encouragement': [
            'أنت قوي', 'تقدر تتجاوز هذا', 'الأمور راح تتحسن',
            'خذ وقتك', 'شوي شوي', 'كل شي له حل'
        ],
        'religious_context': [
            'الله سبحانه وتعالى', 'بإذن الله', 'إن شاء الله',
            'الله يعينك', 'توكل على الله', 'الله معك'
        ],
        'local_terms': [
    'وايد',  # كثير
    'زين',  # جيد
    'شنو',  # ماذا
    'وين',  # أين
    'متى',  # متى
    'ليش'   # لماذا
]

    }

def get_crisis_keywords_omani():
    """Crisis detection keywords in Omani Arabic"""
    
    return [
        # Direct suicide references
        'انتحار', 'أنتحر', 'أقتل نفسي',
        
        # Death wishes
        'أريد أموت', 'أبي أموت', 'ودي أموت',
        'أتمنى أموت', 'ليتني أموت',
        
        # Life ending expressions
        'أنهي حياتي', 'أخلص من الحياة', 'أتخلص من نفسي',
        
        # Exhaustion with life
        'تعبت من الحياة', 'ما عاد فيني أعيش', 'ما أقدر أكمل',
        'خلاص ما أقدر', 'انتهيت', 'ما عاد عندي أمل',
        
        # Omani specific expressions
        'ما عاد فيني', 'خلاص تعبت', 'ما أقدر أتحمل أكثر',
        'أريد أخلص', 'ودي أختفي', 'ما أبي أعيش'
    ]

def get_inappropriate_responses():
    """Responses that should be avoided in Omani cultural context"""
    
    return [
        # Religious inappropriateness
        'حرام عليك تحس كذا', 'الله يعاقبك', 'هذا ذنب',
        
        # Cultural insensitivity
        'هذا عيب', 'الناس شيقولون عنك', 'اخجل من نفسك',
        
        # Gender inappropriateness
        'تكلم مع رجال', 'البنت ما تقول كذا', 'الولد ما يبكي',
        
        # Family disrespect
        'أهلك غلط', 'عائلتك ما تفهم', 'اترك أهلك',
        
        # Medical advice
        'خذ هذا الدواء', 'أنت مريض نفسياً', 'عندك اكتئاب'
    ]
