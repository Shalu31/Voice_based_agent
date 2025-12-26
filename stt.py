import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from faster_whisper import WhisperModel

model = WhisperModel("small", compute_type="int8")

def speech_to_text(audio_path="input.wav"):
    segments, _ = model.transcribe(audio_path, language="hi")
    text = " ".join(seg.text for seg in segments)
    return text.strip()

if __name__ == "__main__":
    text = speech_to_text()
    print("STT completed successfully")   # ASCII ONLY

