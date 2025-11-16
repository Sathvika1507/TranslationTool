# Task 1 — AI Multilingual Translator Tool

Desktop Python app with GUI for translating text and documents using the **MyMemory free translation API**.  
Optional support for **Text-to-Speech (TTS)** using `pyttsx3` and **Speech-to-Text (STT)** using `speech_recognition`.  
Created as part of the **CodeAlpha AI Internship**.

---

## 🌟 Features

- Translate **text** in real-time between multiple languages.
- Translate **.txt documents**.
- **Copy**, **Save**, or **Clear** output easily.
- Optional **TTS** (Speak Output) for translated text.
- Optional **STT** (Voice Input) for capturing speech.
- Translation **history** view and export.
- Professional GUI using **CustomTkinter** (light/dark theme).

---

## 🛠️ Installation Guide

### ✔ Step 1 — Make sure you are using Python 3.11
Check version:

```bash
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 --version
Expected output:
Python 3.11.9
✔ Step 2 — Install Required Packages
Basic install (recommended):
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install customtkinter requests pyttsx3
Optional (for voice input):
brew install portaudio
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 -m pip install pyaudio speechrecognition
✔ Step 3 — Run the App
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 app.py
Or run using the Run button in VS Code.
📁 Project Structure
Task1_TranslationTool_Upgraded/
│── app.py                 # Main Python GUI app
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
└── .vscode/
    └── launch.json        # VS Code run/debug configuration (optional)
🖥️ User Interface Overview
Section	Function
Left Text Box	Enter source text
Right Text Box	Shows translated output
Top Menu	Language selection & translation buttons
Bottom Menu	Copy, Save, Clear, TTS, Voice Input, History
Professional UI	Dark/Light theme auto-switch using CustomTkinter
🌐 API Used
MyMemory Translation API — Free and no API key required.
For professional deployment, you may use:
Google Cloud Translate
DeepL
Azure Translator
🎤 How to Give a Demo
Translate a sentence or paragraph.
Show document translation from a .txt file.
Use Speak Output (if pyttsx3 installed).
Display Translation History.
Save output text to a file.
Explain:
UI → API call → response handling → history → optional speech features.
🧑‍💻 Technologies Used
Python 3.11
CustomTkinter
Requests
Pyttsx3 (optional TTS)
SpeechRecognition + PyAudio (optional STT)
📦 requirements.txt
customtkinter
requests
pyttsx3
# Optional speech features:
speechrecognition
pyaudio
© Credits
Created by Bogam Sathvika
As part of CodeAlpha AI Internship — Task 1

