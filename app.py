from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Put your OpenAI API key here

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_message = req['queryResult']['queryText']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    chatbot_reply = response['choices'][0]['message']['content']

    return jsonify({
        'fulfillmentText': chatbot_reply
    })

if __name__ == '__main__':
    app.run()
