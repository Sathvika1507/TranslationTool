"""
AI Multilingual Translator App
- Desktop app using customtkinter
- Uses MyMemory free API for translation (no API key)
- Optional: pyttsx3 for TTS, speech_recognition for STT
- Document translation for .txt files
- History saved in memory and downloadable as file
"""

import os
import json
import requests
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

# Optional imports guarded
try:
    import pyttsx3
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

try:
    import speech_recognition as sr
    STT_AVAILABLE = True
except Exception:
    STT_AVAILABLE = False

APP_TITLE = "CodeAlpha — AI Multilingual Translator (Upgraded)"

# Languages dictionary — friendly name to code
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
}

# Simple helpers
def mymemory_translate(text, src="auto", tgt="en"):
    """
    Call MyMemory free API. Returns translated text or raises.
    """
    # encode text for URL safely using requests params
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text, "langpair": f"{src}|{tgt}"}
    resp = requests.get(url, params=params, timeout=10)
    data = resp.json()
    # prefer responseData.translatedText
    translated = data.get("responseData", {}).get("translatedText", "")
    return translated

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title(APP_TITLE)
        master.geometry("880x620")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Containers
        self.frame_top = ctk.CTkFrame(master)
        self.frame_top.pack(fill="x", padx=12, pady=8)

        self.frame_middle = ctk.CTkFrame(master)
        self.frame_middle.pack(fill="both", expand=True, padx=12, pady=(0,8))

        # Top controls
        self.src_var = ctk.StringVar(value="Auto Detect")
        self.tgt_var = ctk.StringVar(value="English")
        ctk.CTkLabel(self.frame_top, text="Source").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.src_menu = ctk.CTkComboBox(self.frame_top, values=list(LANGUAGES.keys()), variable=self.src_var, width=200)
        self.src_menu.grid(row=0, column=1, padx=6, pady=6)

        ctk.CTkLabel(self.frame_top, text="Target").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        self.tgt_menu = ctk.CTkComboBox(self.frame_top, values=list(LANGUAGES.keys()), variable=self.tgt_var, width=200)
        self.tgt_menu.grid(row=0, column=3, padx=6, pady=6)

        self.translate_btn = ctk.CTkButton(self.frame_top, text="Translate (Text)", command=self.translate_text)
        self.translate_btn.grid(row=0, column=4, padx=10, pady=6)

        self.translate_file_btn = ctk.CTkButton(self.frame_top, text="Translate .txt File", command=self.translate_file)
        self.translate_file_btn.grid(row=0, column=5, padx=6, pady=6)

        # Middle: two large text panes
        self.input_box = ctk.CTkTextbox(self.frame_middle, width=420, height=340)
        self.input_box.grid(row=0, column=0, padx=(6,12), pady=12)

        self.output_box = ctk.CTkTextbox(self.frame_middle, width=420, height=340)
        self.output_box.grid(row=0, column=1, padx=(12,6), pady=12)

        # Bottom control row
        self.frame_bottom = ctk.CTkFrame(master)
        self.frame_bottom.pack(fill="x", padx=12, pady=(0,12))

        self.copy_btn = ctk.CTkButton(self.frame_bottom, text="Copy Output", command=self.copy_output)
        self.copy_btn.grid(row=0, column=0, padx=6, pady=6)
        self.save_btn = ctk.CTkButton(self.frame_bottom, text="Save Output", command=self.save_output)
        self.save_btn.grid(row=0, column=1, padx=6, pady=6)
        self.clear_btn = ctk.CTkButton(self.frame_bottom, text="Clear", command=self.clear_all)
        self.clear_btn.grid(row=0, column=2, padx=6, pady=6)

        # TTS / STT buttons
        if TTS_AVAILABLE:
            self.tts_btn = ctk.CTkButton(self.frame_bottom, text="Speak Output", command=self.speak_output)
        else:
            self.tts_btn = ctk.CTkButton(self.frame_bottom, text="Speak Output (install pyttsx3)", state="disabled")
        self.tts_btn.grid(row=0, column=3, padx=6, pady=6)

        if STT_AVAILABLE:
            self.stt_btn = ctk.CTkButton(self.frame_bottom, text="Voice Input", command=self.voice_input)
        else:
            self.stt_btn = ctk.CTkButton(self.frame_bottom, text="Voice Input (install speech_recognition+pyaudio)", state="disabled")
        self.stt_btn.grid(row=0, column=4, padx=6, pady=6)

        # History area (right side)
        self.history = []
        self.history_btn = ctk.CTkButton(self.frame_bottom, text="Show History", command=self.show_history)
        self.history_btn.grid(row=0, column=5, padx=6, pady=6)

        # Status bar
        self.status = ctk.CTkLabel(master, text="Ready", anchor="w")
        self.status.pack(fill="x", padx=12, pady=(0,8))

        # Initialize TTS engine if available
        self.engine = None
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
            except Exception:
                self.engine = None

    def set_status(self, txt):
        self.status.configure(text=txt)
        self.master.update_idletasks()

    def translate_text(self):
        txt = self.input_box.get("0.0", "end").strip()
        if not txt:
            messagebox.showinfo("Info", "Enter text to translate or try file translation.")
            return
        src = LANGUAGES.get(self.src_var.get(), "auto")
        tgt = LANGUAGES.get(self.tgt_var.get(), "en")
        self.set_status("Translating...")

        def worker():
            try:
                translated = mymemory_translate(txt, src=src, tgt=tgt)
                self.output_box.delete("0.0", "end")
                self.output_box.insert("0.0", translated)
                self.history.append({"src": txt, "translated": translated, "src_lang": src, "tgt_lang": tgt})
                self.set_status("Translation complete")
            except Exception as e:
                self.set_status("Error")
                messagebox.showerror("Error", f"Translation failed: {e}")

        threading.Thread(target=worker, daemon=True).start()

    def translate_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")
            return
        self.input_box.delete("0.0", "end")
        self.input_box.insert("0.0", content)
        self.translate_text()

    def copy_output(self):
        txt = self.output_box.get("0.0", "end").strip()
        if txt:
            self.master.clipboard_clear()
            self.master.clipboard_append(txt)
            messagebox.showinfo("Copied", "Translated text copied to clipboard")

    def save_output(self):
        txt = self.output_box.get("0.0", "end").strip()
        if not txt:
            messagebox.showinfo("Info", "No output to save")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(txt)
                messagebox.showinfo("Saved", f"Saved to {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def clear_all(self):
        self.input_box.delete("0.0", "end")
        self.output_box.delete("0.0", "end")

    def speak_output(self):
        if not self.engine:
            messagebox.showinfo("Not available", "TTS engine is not available.")
            return
        txt = self.output_box.get("0.0", "end").strip()
        if not txt:
            messagebox.showinfo("Info", "No text to speak")
            return
        self.set_status("Speaking...")
        def tts_worker():
            try:
                self.engine.say(txt)
                self.engine.runAndWait()
            except Exception as e:
                messagebox.showerror("Error", f"TTS failed: {e}")
            finally:
                self.set_status("Ready")
        threading.Thread(target=tts_worker, daemon=True).start()

    def voice_input(self):
        if not STT_AVAILABLE:
            messagebox.showinfo("Not available", "Speech recognition libraries are not installed.")
            return
        # Use speech_recognition to capture microphone and insert text
        r = sr.Recognizer()
        mic = sr.Microphone()
        self.set_status("Listening...")
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=6)
        self.set_status("Recognizing...")
        try:
            text = r.recognize_google(audio)
            self.input_box.delete("0.0", "end")
            self.input_box.insert("0.0", text)
            self.set_status("Ready")
        except Exception as e:
            messagebox.showerror("Error", f"Speech recognition failed: {e}")
            self.set_status("Ready")

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No translations yet")
            return
        hwin = ctk.CTkToplevel(self.master)
        hwin.title("Translation History")
        hwin.geometry("640x420")
        listbox = ctk.CTkTextbox(hwin, width=600, height=360)
        listbox.pack(padx=12, pady=12, fill="both", expand=True)
        for item in reversed(self.history):
            listbox.insert("0.0", f"Source ({item['src_lang']})->Target ({item['tgt_lang']})\n{item['src']}\n=>\n{item['translated']}\n\n")

def main():
    root = ctk.CTk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
