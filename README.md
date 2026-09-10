# Orion
Orion is an AI personal assistant made by evolyx.
Here is the stack:
- openWakeWord - Monitors for "Hey Orion" to be said to make the model start listening.
- faster-whisper - Speech to text; sends speech to Groq to be processed.
- Groq - Takes text from faster-whisper and processes it with an AI model, generating a response to the question and sending it back with API calls. Groq then takes the output and processes it into an audio file, which is downloaded by the client and played.
