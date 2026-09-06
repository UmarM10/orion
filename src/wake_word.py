"""

# Orion - Wake Word Processing
This script processes the wake word using openwakeword and starts text to speech once it is triggered.
Since Orion is under development, currently the wake word will be "Hey Jarvis".

"""

import openwakeword
from openwakeword.model import Model
import pyaudio
import numpy
