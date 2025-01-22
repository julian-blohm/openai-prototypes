from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Check out documentation here: https://platform.openai.com/docs/guides/embeddings/
response = client.embeddings.create(
    input = "Michael Joardan is better than LeBron James",
    model = "text-embedding-3-small"
)

print(response.data[0].embedding)