from pprint import pprint
from .utils import post_facebook_message, post_facebook_message_sair, post_facebook_message_date, \
    post_facebook_message_checkin
import urllib.request
import json
from django.conf import settings
import re

list_oi = ['Ola', 'oi', 'Oi', 'OI', 'oI']


def test(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            if message['message']['text'] in list_oi:
                with urllib.request.urlopen(
                        f"https://graph.facebook.com/{message['sender']['id']}?fields=first_name,last_name,profile_pic&access_token={settings.ACCESS_TOKEN}") as url:
                    first_name = json.loads(url.read().decode('utf-8'))
                    pprint(first_name)
                post_facebook_message(message['sender']['id'], first_name['first_name'])
            else:
                pass
            if 'Sair' in message['message']['text']:
                with urllib.request.urlopen(
                        f"https://graph.facebook.com/{message['sender']['id']}?fields=first_name,last_name,profile_pic&access_token={settings.ACCESS_TOKEN}") as url:
                    first_name = json.loads(url.read().decode('utf-8'))
                    pprint(first_name)
                post_facebook_message_sair(message['sender']['id'], first_name['first_name'])
            elif re.match(r'\d\d/\d\d/\d\d', f"{message['message']['text']}") or re.match(r'\d\d/\d\d/\d\d\d\d',
                                                                                          f"{message['message']['text']}"):
                with urllib.request.urlopen(
                        f"https://graph.facebook.com/{message['sender']['id']}?fields=first_name,last_name,profile_pic&access_token={settings.ACCESS_TOKEN}") as url:
                    first_name = json.loads(url.read().decode('utf-8'))
                    pprint(first_name)
                post_facebook_message_date(message['sender']['id'], first_name['first_name'])
            elif 'Data Check-in' in message['message']['text']:
                with urllib.request.urlopen(
                        f"https://graph.facebook.com/{message['sender']['id']}?fields=first_name,last_name,profile_pic&access_token={settings.ACCESS_TOKEN}") as url:
                    first_name = json.loads(url.read().decode('utf-8'))
                    pprint(first_name)
                post_facebook_message_checkin(message['sender']['id'], first_name['first_name'])
            else:
                pass
