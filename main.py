from record_audio import record_audio
from stt import speech_to_text
from tts import speak

from agents.memory import Memory
from agents.planner import planner
from agents.executor import executor
from agents.evaluator import evaluator

memory = Memory()

while True:
    record_audio()
    user_text = speech_to_text()

    if not user_text:
        speak("माफ़ कीजिए, आपकी आवाज़ समझ नहीं आई।")
        continue

    # VERY SIMPLE PARSING (ENOUGH FOR DEMO)
    if "उम्र" in user_text or "साल" in user_text:
        number = int("".join(filter(str.isdigit, user_text)))
        memory.set("age", number)
        speak("उम्र दर्ज कर ली गई है।")
        continue

    if "आय" in user_text or "लाख" in user_text:
        number = int("".join(filter(str.isdigit, user_text)))
        memory.set("income", number * 100000)
        speak("आय दर्ज कर ली गई है।")
        continue

    step = planner(memory)

    if step["action"] == "ask_age":
        speak("कृपया अपनी उम्र बताइए।")

    elif step["action"] == "ask_income":
        speak("कृपया अपनी वार्षिक आय बताइए।")

    elif step["action"] == "check_eligibility":
        result = executor(memory)
        status = evaluator(result)

        if status == "SUCCESS":
            speak("आप इन योजनाओं के पात्र हैं: " + " और ".join(result))
        else:
            speak("आप किसी योजना के पात्र नहीं हैं।")

        break
