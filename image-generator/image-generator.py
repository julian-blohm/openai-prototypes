from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_picture():
    response = client.images.generate(
        model="dall-e-3",
        prompt="fat hamster in comic style doing sky diving",
        size="1024x1024"
    )
    return response.data[0].url

image_url = generate_picture()

print("Generated image URL: ", image_url)