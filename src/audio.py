import pyaudio

"""

Audio utilities.

"""

p = pyaudio.PyAudio()

microphone_stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True
)
microphone_stream.start_stream()
print("Microphone stream started.")
