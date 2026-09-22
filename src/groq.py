"""

Groq API Interface module.

"""

from groq import Groq

class GroqAPI:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
