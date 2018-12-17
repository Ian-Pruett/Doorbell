from flask import request, jsonify, Blueprint
from bot import NotifyBot

notify = Blueprint('notify', __name__)

@notify.route('/notify', methods=['POST'])
def notify():
    content = request.get_json()
    bot = NotifyBot(content.botEmail, content.botPassword)
    bot.ring()
    return jsonify({'status': 1}), 200

