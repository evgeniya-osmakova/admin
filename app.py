from flask import Flask
from flask_cors import CORS
from flask import Response
from flask import request
from flask import abort
import sys
import json

app = Flask(__name__)
CORS(app)


cards = [
    {"id": "1", "header": "Getting Started", "description": "Learn how CodesFord works and how to start learning." },
    {"id": "2", "header": "Account", "description": "Manage your account settings." },
    {"id": "3", "header": "Courses", "description": "Everything about taking a course on CodesFord." },
    {"id": "4", "header": "Purchase/Refunds", "description": "Learn about payment, how to send gifts, and refunds." }
]

@app.route('/', methods=['GET'])
def get_root():
    return ''

# get card list
@app.route('/cards/', methods=['GET'])
def get_cards():
    return json.dumps(cards)

# add new card
@app.route('/cards/', methods=['POST'])
def post_cards():
    new_card = json.loads(request.data)

    max_id = 0
    for card in cards:
        if int(card['id']) > max_id:
            max_id = int(card['id'])

    new_card['id'] = str(max_id + 1)
    cards.append(new_card)
    return new_card

# delete card
@app.route('/cards/<id>', methods=['DELETE'])
def delete_card(id):
    for i in range(len(cards)):
        card = cards[i]
        if card['id'] == id:
            del cards[i]
            return card
    abort(404)


# change the card
@app.route('/cards/', methods=['PUT'])
def put_card():
    card_to_amend = json.loads(request.data)
    for i in range(len(cards)):
        card = cards[i]
        if card['id'] == card_to_amend['id']:
            cards[i] = card_to_amend
            return card
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)