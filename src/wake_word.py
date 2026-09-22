"""

# Orion - Wake Word Processing
This script processes the wake word using openwakeword and starts text to speech once it is triggered.

"""

import time
import warnings
from decimal import Decimal
from pathlib import Path

import numpy
from openwakeword.model import Model

from audio import microphone_stream as mic

# Ignore onnxruntime fallback warnings
warnings.filterwarnings("ignore", category=UserWarning, module="onnxruntime")

# "Hey Orion" custom trained model - ./hey_orion.tflite
model = Model(
    wakeword_model_paths=[str(Path(__file__).parent / "models" / "hey_orion.onnx")]
)


def listen(debug=False):
    # Blocking function
    # On successful trigger, return confidence percentage as a float.

    prediction = None
    while True:
        try:
            raw_frame = mic.read(num_frames=1280)
            frame = numpy.frombuffer(raw_frame, dtype=numpy.int16)
            prediction = model.predict(frame)
            if prediction["hey_orion"] >= numpy.float32(0.5):
                model.reset()
                if debug:
                    print(
                        f"Wake word triggered with {round(Decimal(str(prediction['hey_orion'])), 2)}% confidence."
                    )
                break
        except KeyboardInterrupt:
            print(" Interrupted: Exiting...")
            return None

    if prediction:
        return round(Decimal(str(prediction["hey_orion"])), 2) * 100


# Test script - runs only if executed directly.
if __name__ == "__main__":
    print("Test - Listening for 'Hey Orion' above 50% confidence.")
    while True:
        if listen(debug=True):
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print(" Interrupted: Exiting...")
                break
        else:
            break
