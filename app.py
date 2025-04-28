from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Updated user's real DeepAI API Key
DEEPAI_API_KEY = "7c7e8e85-4c1f-45ef-b859-0b5e56b19afe"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_message = req['queryResult']['queryText']

    response = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={'text': user_message},
        headers={'api-key': DEEPAI_API_KEY}
    )

    response_json = response.json()
    chatbot_reply = response_json.get('output', "Sorry, I couldn't understand that.")

    return jsonify({
        'fulfillmentText': chatbot_reply
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
