from gtts import gTTS
import os

from huggingface_hub import Agent

def speak(text):
    
    tts = gTTS(text=text, lang="hi")
    tts.save("response.mp3")
    os.system("start response.mp3")  # Windows

if __name__ == "__main__":
    speak("नमस्ते, मैं आपकी मदद कर सकता हूँ")