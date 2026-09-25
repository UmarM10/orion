"""

Speech to text. Records audio and locally text used by Groq.

"""

import sys
import time

import groq
import numpy as np
import pyaudio
import torch
from silero_vad import VADIterator, load_silero_vad

from audio import microphone_stream as mic

# Cutoff time in seconds
CUTOFF_TIME=2

def record(debug=False):
    # Blocking function
    # Records audio until Silero VAD detects silence, then returns path to the recorded audio file.
    model = load_silero_vad()
    vad_iterator = VADIterator(model, sampling_rate=16000)

    recorded_frames = []
    has_spoken = False
    silence_start_time = None

    while True:
        try:
            raw_frame = mic.read(512)
            recorded_frames.append(raw_frame)

            np_frame = np.frombuffer(raw_frame, dtype=np.int16).astype(np.float32) / 32768.0
            frame = torch.from_numpy(np_frame)
            result = vad_iterator(frame, return_seconds=True)

            concluded_waiting = False
            restart_speech_trigger = False

            if result:
                if "start" in result:
                    if debug:
                        print("Speech resumed." if has_spoken else "Speech started.")
                    has_spoken = True
                    silence_start_time = None

                elif "end" in result:
                    if debug:
                        print("Speech paused, waiting for further input before concluding.")
                    silence_start_time = time.time()

            if has_spoken and silence_start_time is not None:
                if time.time() - silence_start_time >= CUTOFF_TIME:
                    if debug:
                        print("Extended silence detected, stopping recording.")
                    break
        except KeyboardInterrupt:
            print(" Interrupted: Exiting...")
            sys.exit(0)
    return b"".join(recorded_frames)


if __name__ == "__main__":
    # Test when run directly
    print("Testing Silero Voice Activation Detection.")
    record(debug=True)
