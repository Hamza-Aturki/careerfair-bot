from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Hardcoded API key for now (you should replace this later for better security)
openai.api_key = "YOUR_OPENAI_API_KEY"

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
