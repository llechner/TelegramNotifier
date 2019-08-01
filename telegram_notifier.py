import json
import requests
import urllib
import sys

TOKEN = "YOURTOKEN"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def main(argv):

    if len(argv) > 1:
        text = argv[1]
    else:
        text = "default"

    id = "YOURID"
    send_message(text, id)


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
    print "getting url: " + url
    get_url(url)


if __name__ == '__main__':
    main(sys.argv)
