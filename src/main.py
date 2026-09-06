"""

╭--------------------------------------------------╮
| ███████╗██╗   ██╗ ██████╗ ██╗  ██╗   ██╗██╗  ██╗ |
| ██╔════╝██║   ██║██╔═══██╗██║  ╚██╗ ██╔╝╚██╗██╔╝ |
| █████╗  ██║   ██║██║   ██║██║   ╚████╔╝  ╚███╔╝  |
| ██╔══╝  ╚██╗ ██╔╝██║   ██║██║    ╚██╔╝   ██╔██╗  |
| ███████╗ ╚████╔╝ ╚██████╔╝███████╗██║   ██╔╝ ██╗ |
| ╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝ |
╰--------------------- Orion ----------------------╯

Orion is an AI personal assistant made by evolyx.
Here is the stack:
    - openWakeWord - Monitors for "Orion" to be said to make the model start listening.
    - faster-whisper - Speech to text; sending speech to the model to be processed.
    - Groq - Takes text from faster-whisper and processes it with an AI model, generating a response to the question and sending it back with API calls.
    - Piper - Text to speech; taking the result from Groq and turning it into audio.

"""
import wake_word
