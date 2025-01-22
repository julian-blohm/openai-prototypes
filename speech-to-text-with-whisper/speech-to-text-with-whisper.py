from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# audio file (just execute the text-to-speech-with-gTTS to generate one)
audio_file = open("./example.mp3", "rb")

# transcribe
transcribe = client.audio.transcriptions.create(
    model = "whisper-1",
    file = audio_file
)

print(transcribe.text)