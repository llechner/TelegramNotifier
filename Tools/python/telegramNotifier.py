import json
import requests
import urllib

from TelegramNotifier.Tools.user import telegramBotToken, telegramUserID

URL = "https://api.telegram.org/bot{}/".format(telegramBotToken)

def send( text ):
    send_message(text, telegramUserID)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


if __name__ == '__main__':

    import sys
    text = " ".join( sys.argv[1:] ) if len( sys.argv ) > 1 else "test"
    send( text )
