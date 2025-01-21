from openai import OpenAI

import os

import pandas as pd

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# read csv file downloaded from https://www.kaggle.com/datasets/ and provide output
dataset = pd.read_csv("./filelocation.csv") # adjust filelocation when using

def analyze_data(dataset):
    response = client.chat.completions.create(
        model = "o1",
        messages = [{"role":"user", "content":f"You are a research assistant. Provide key insights from {dataset} in point form."}],
        max_tokens = 500,
        temperature = 0.2
    )

    return response.choices[0].message.content


print(analyze_data(dataset))
