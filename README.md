# 🌐 AI Multilingual Translator (Upgraded Version)
### CodeAlpha Internship Project — Task 1

A modern, polished, and user-friendly multilingual translator app built using **CustomTkinter**.  
This upgraded version includes text translation, document translation, history tracking, and optional speech features.

---

## 🚀 Features

### ✨ Core Functionalities
- Translate text between multiple languages  
- Auto language detection  
- Clean and modern **CustomTkinter** GUI  
- Input & output text panels  
- Copy output  
- Save translated text  
- Translation history window  
- Status bar for real-time updates  

---

### 📄 Document Translation
- Translate `.txt` files instantly  
- Load → Translate → Save output  

---

### 🔊 Optional Speech Features
*(These features work only if additional packages are installed.  
If not installed, buttons remain disabled — the app still works completely.)*

- **Text-to-Speech (TTS)** using `pyttsx3`  
- **Speech-to-Text (Voice Input)** using `speech_recognition` + microphone  

---

## 🛠️ Installation Guide

### ✔ Step 1 — Make sure you are using Python **3.11**
Check version:

```bash
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 --version
You should see:
Python 3.11.9


✔ Step 2 — Install Required Packages
Basic install (recommended)
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install customtkinter requests pyttsx3

Optional (for voice input)
brew install portaudio
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install pyaudio speechrecognition


✔ Step 3 — Run the App
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 app.py

OR run using the Run button in VS Code.

📁 Project Structure
Task1_TranslationTool_Upgraded/
│── app.py
│── requirements.txt
│── README.md
└── .vscode/
    └── launch.json


📦 requirements.txt
customtkinter
requests
pyttsx3
# Optional speech features:
speechrecognition
pyaudio


🖥️ User Interface Overview


Left Text Box → Enter text


Right Text Box → Output translation


Top Menu → Language selection & translation buttons


Bottom Menu → Copy, Save, Clear, TTS, Voice Input, History


Professional appearance using CustomTkinter (auto dark/light theme)



🌐 API Used
This app uses the MyMemory Translation API — a free, no-key translation API.
For professional deployments, you may replace it with:


Google Cloud Translate


DeepL


Azure Translator



🎤 How to Give Demo (For Internship / Interview)


Translate a sentence


Show document translation


Use “Speak Output” (if pyttsx3 installed)


Display “Translation History”


Save output text to a file


Explain:


UI → API call → response handling → history → optional speech




This demonstrates strong skills in Python, GUI, APIs, and real-time user apps.

🧑‍💻 Technologies Used


Python 3.11


CustomTkinter


Requests


Pyttsx3 (optional TTS)


SpeechRecognition + PyAudio (optional STT)



© Credits
Created by Bogam Sathvika
as part of CodeAlpha AI Internship — Task 1

