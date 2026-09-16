# Orion
Orion is a personal AI voice assistant made by evolyx.
Here is the stack:
    - openWakeWord - Monitors for "Hey Orion" to be said to make the model start listening.
    - Groq - Takes text from the audio stream and processes it with an AI model, generating a response to the question and sending it back with API calls. Groq then takes the output and processes it into an audio file, which is downloaded by the client and played.
