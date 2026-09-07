"""

# Orion - Wake Word Processing
This script processes the wake word using openwakeword and starts text to speech once it is triggered.

"""

import openwakeword
from openwakeword.model import Model
import pyaudio
import sounddevice as sd
import numpy
from decimal import Decimal
from pathlib import Path
from datetime import datetime
import time
import warnings

# Ignore onnxruntime fallback warnings
warnings.filterwarnings("ignore", category=UserWarning, module="onnxruntime")

# "Hey Orion" custom trained model - ./hey_orion.tflite
model = Model(wakeword_model_paths=[str(Path(__file__).parent / "models" / "hey_orion.onnx")])

p = pyaudio.PyAudio()
audio_stream = p.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True)
audio_stream.start_stream()
print("Opened microphone stream: Listening for 'Hey Orion' above 50% confidence.")

# Test script - runs only if executed directly.
if __name__ == "__main__":
    # On successful trigger, print "TRIGGERED" with a timestamp.
    while True:
        try:
            raw_frame = audio_stream.read(num_frames=1280)
            frame = numpy.frombuffer(raw_frame, dtype=numpy.int16)
            prediction = model.predict(frame)
            if prediction["hey_orion"] >= numpy.float32(0.5):
                model.reset()
                print(f"TRIGGERED - {round(Decimal(str(prediction["hey_orion"])), 2) * 100}% confidence.")
        except KeyboardInterrupt:
            print(" Interrupted: Exiting...")
            break

    audio_stream.stop_stream()
    audio_stream.close()

def listen():
    # On successful trigger, return confidence percentage as a float.
    while True:
        try:
            raw_frame = audio_stream.read(num_frames=1280)
            frame = numpy.frombuffer(raw_frame, dtype=numpy.int16)
            prediction = model.predict(frame)
            if prediction["hey_orion"] >= numpy.float32(0.5):
                model.reset()
                return round(Decimal(str(prediction["hey_orion"])), 2) * 100
        except KeyboardInterrupt:
            return
            break
