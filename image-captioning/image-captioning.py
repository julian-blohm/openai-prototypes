from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

image_url = "https://sm.ign.com/ign_de/screenshot/default/onepiece_8b3q.png"

def generate_captions(image_url):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{
            "role":"user","content":[
                {"type":"text", "text":"What is this image?"},
                {"type":"image_url", "image_url":{"url":image_url}}]}],
        max_tokens = 125
    )
    return response.choices[0].message.content

print(generate_captions(image_url))