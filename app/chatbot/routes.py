from flask import request, jsonify, Blueprint
from flask_cors import CORS
from app.chatbot.bot import NotifyBot


notify = Blueprint('notify', __name__)


@notify.route('/notify', methods=['POST'])
def alert():
    content = request.get_json()
    email = content['BotEmail']
    password = content['BotPassword']
    bot = NotifyBot(email, password)
    bot.ring()
    return jsonify({'status': 1}), 200