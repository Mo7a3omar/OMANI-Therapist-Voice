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
