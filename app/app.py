from flask import Flask, render_template, request, jsonify
import openai
import os

# OpenAI Key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


# Not working now
@app.route('/generate_story')
def generate_story():
    data = request.get_json()
    user_input = data['input']

    # Send user input to ChatGPT
    response = send_message(user_input)

    return jsonify({'response': response})


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']

    response = send_message(message)

    return response


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


if __name__ == '__main__':
    app.run(debug=True)
