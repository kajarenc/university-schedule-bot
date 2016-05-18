#!/usr/bin/env python
import sys
import os
import os

import MySQLdb
import webapp2


CLOUDSQL_PROJECT = 'university-schedule-bot'
CLOUDSQL_INSTANCE = 'database'

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages/'))

from flask import Flask, request
import telegram

app = Flask(__name__)
from bot_logic import handler

bot = telegram.Bot(token='234777824:AAGL3fWSKxGuRR8oENhu7Jo-3EhvYKRH_P8')
db = MySQLdb.connect(
    unix_socket='/cloudsql/{}:{}'.format(
        CLOUDSQL_PROJECT,
        CLOUDSQL_INSTANCE),
    user='root')

def get_random_joke():
    return "random joke"


@app.route('/234777824:AAGL3fWSKxGuRR8oENhu7Jo-3EhvYKRH_P8', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        handler(bot, update,db)
    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://university-schedule-bot.appspot.com/234777824:AAGL3fWSKxGuRR8oENhu7Jo-3EhvYKRH_P8')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'

# IPv4 address
#
# You will be charged $0.01 each hour the instance is inactive and has an IPv4 address assigned.
#
# 173.194.236.83