import os
import openai

# Add OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_message(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
    )

    if response.choices:
        return response.choices[0].message.content.strip()
    else:
        return "Sorry, I didn't get that."


print("ChatGPT: Hi! How can I assist you today?")
while True:
    user_input = input("User: ")
    response = send_message(user_input)
    print("ChatGPT: " + response)
