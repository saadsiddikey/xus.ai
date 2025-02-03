import openai

openai.api_key = "your_openai_api_key"

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

while True:
    user_input = input("Ask me anything: ")
    if user_input.lower() == "exit":
        break
    answer = chat_with_ai(user_input)
    print("Xus.AI:", answer)
