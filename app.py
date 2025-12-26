import streamlit as st
import os

from record_audio import record_audio
from stt import speech_to_text
from tts import speak

from agents.memory import Memory
from agents.planner import planner
from agents.executor import executor
from agents.evaluator import evaluator

# ------------------------
# Streamlit UI
# ------------------------

st.set_page_config(page_title="Hindi Government Scheme Agent")

st.title("🎙️ Hindi Voice-Based Government Scheme Agent")

st.write("This is a voice-first AI agent that helps users find eligible government schemes.")

if "memory" not in st.session_state:
    st.session_state.memory = Memory()

if st.button("🎤 Start Voice Interaction"):
    st.write("Recording voice...")

    record_audio()
    user_text = speech_to_text()

    if not user_text:
        st.write("Speech not understood.")
        speak("माफ़ कीजिए, आपकी आवाज़ समझ नहीं आई।")

    else:
        mem = st.session_state.memory

        # VERY SIMPLE INFO EXTRACTION (FOR DEMO)
        if "उम्र" in user_text or any(char.isdigit() for char in user_text):
            nums = "".join(filter(str.isdigit, user_text))
            if nums:
                mem.set("age", int(nums))
                speak("उम्र दर्ज कर ली गई है।")

        elif "आय" in user_text or "लाख" in user_text:
            nums = "".join(filter(str.isdigit, user_text))
            if nums:
                mem.set("income", int(nums) * 100000)
                speak("आय दर्ज कर ली गई है।")

        step = planner(mem)

        if step["action"] == "ask_age":
            speak("कृपया अपनी उम्र बताइए।")

        elif step["action"] == "ask_income":
            speak("कृपया अपनी वार्षिक आय बताइए।")

        elif step["action"] == "check_eligibility":
            result = executor(mem)
            status = evaluator(result)

            if status == "SUCCESS":
                speak("आप इन योजनाओं के पात्र हैं: " + " और ".join(result))
            else:
                speak("आप किस योजना के पात्र नहीं हैं।")
