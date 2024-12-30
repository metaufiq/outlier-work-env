
from flask import Flask, request, jsonify   

import random


app = Flask(__name__)
  
@app.route('/chat', methods=['POST'])

def chat():

    user_input = request.json.get('message')

    response = process_input(user_input)

    return jsonify({'response': response})
def process_input(user_input):

    responses = ["Hello!", "How can I assist you?", "I'm here to help!"]

    return random.choice(responses)

if __name__ == '__main__':

    app.run(debug=True)
