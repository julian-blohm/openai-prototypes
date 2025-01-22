import os

# https://gtts.readthedocs.io/en/latest/
from gtts import gTTS

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# prompt
prompt = "Tell me a story about a brave knight that loves chicken wings"

# handle text to speech
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("tts_example.mp3")
    os.system("afplay tts_example.mp3")

# generate text
def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.8,
        max_tokens=150
    )
    return response.choices[0].message.content


def gen_and_speak(prompt):
    text=generate_text(prompt)
    print("Generated Text: '\n", text)
    text_to_speech(text)

print(gen_and_speak(prompt))