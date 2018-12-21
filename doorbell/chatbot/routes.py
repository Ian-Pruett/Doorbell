import os
from flask import request, jsonify, Blueprint
from flask_cors import CORS
from doorbell.chatbot.bot import NotifyBot


notify = Blueprint('notify', __name__)


@notify.route('/notify', methods=['POST'])
def alert():
    content = request.get_json()
    email = content['BotEmail']
    password = content['BotPassword']
    k = content['key']
    if k != str(os.environ.get('SECRET_KEY')):
        return jsonify({'status': -1}), 200
    try:
        bot = NotifyBot(email, password, max_tries=2)
        bot.ring()
        return jsonify({'status': 1}), 200
    except:
        return jsonify({'status': 0}), 200