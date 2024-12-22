from openai import OpenAI

client = OpenAI(
    api_key = "<add your key here>"
)

ingredients = []

while True:
    ingredient = input("Enter your ingredients. Type done once complete:")
    if ingredient.lower() == "done":
        break

    ingredients.append(ingredient)

prompt = "hello"


def recipe_gen(ingredients):

    messages = []

    for ingredient in ingredients:
        messages.append({"role": "user", "content": ingredient})

    messages.extend([
        {"role": "system", "content": "direct, point"},
        {"role": "assistant", "content": "You are a high-end chef. Generate a recipe based on the given ingredients"}
    ])

    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages,    
        max_tokens = 300,
        temperature = 0.9
    )

    return response.choices[0].message.content


print(recipe_gen(ingredients))
