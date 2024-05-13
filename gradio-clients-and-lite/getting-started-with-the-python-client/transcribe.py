"""
transcribe.py (Guides, Gradio Clients And Lite,
               Getting Started With The Python Client)
transcribe audio files programmatically
"""

from gradio_client import Client, file

client = Client("abidlabs/whisper")

print(client.predict(audio=file("audio_sample.wav")))
