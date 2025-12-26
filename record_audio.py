import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("Speak now (Hindi)...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Audio recorded successfully")

if __name__ == "__main__":
    record_audio()
