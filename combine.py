from record_audio import record_audio
from stt import speech_to_text
from tts import speak

while True:
    record_audio()
    user_text = speech_to_text()

    if not user_text:
        speak("माफ़ कीजिए, आपकी आवाज़ समझ नहीं आई।")
        continue

    if "बंद" in user_text:
        speak("धन्यवाद, फिर मिलेंगे।")
        break

    speak(f"आपने कहा: {user_text}")
