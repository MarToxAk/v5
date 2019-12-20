import json
import requests
from django.conf import settings
from pprint import pprint
import datetime


def post_facebook_message(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "messaging_type": "RESPONSE",
                        "message": {
                            "text": f"*BOT ILHA BABY*: Bem-Vindo {first_name} a ILHA BABY. Ecolha uma das opções abaixo.",
                            "quick_replies":[
                            {
                                "content_type": "text",
                                "title": "Quero Comprar",
                                "payload": "comprar",
                                "image_url": "https://cdn.icon-icons.com/icons2/67/PNG/512/shoppingcart_compra_13339.png"
                            }, {
                                "content_type": "text",
                                "title": "Data Check-in",
                                "payload": "Check-in",
                                "image_url": "https://www.netclipart.com/pp/m/104-1044961_calendar-icon-png-date-events-icon-white-png.png"
                            }, {
                                "content_type": "text",
                                "title": "Sair",
                                "payload": "sair",
                                "image_url": "https://cdn3.iconfinder.com/data/icons/interface/100/close_button_2-512.png"
                            }
                        ]
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())
def post_facebook_message_sair(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "attachment": {
                                "type": "template",
                                "payload": {
                                    "template_type": "generic",
                                    "elements": [
                                        {
                                            "title": "Welcome!",
                                            "image_url": "https://petersfancybrownhats.com/company_image.png",
                                            "subtitle": "We have the right hat for everyone.",
                                            "default_action": {
                                                "type": "web_url",
                                                "url": "https://petersfancybrownhats.com/view?item=103",
                                                "webview_height_ratio": "tall",
                                            },
                                            "buttons": [
                                                {
                                                    "type": "web_url",
                                                    "url": "https://petersfancybrownhats.com",
                                                    "title": "View Website"
                                                }, {
                                                    "type": "postback",
                                                    "title": "Start Chatting",
                                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())

def post_facebook_message_checkin(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "text": f"*BOT ILHA BABY*: Agora {first_name}, Digite a data que você quer entrar no seguinte formato DD/MM/AAAA.(Exemplo:. {datetime.date.strftime(datetime.date.today(), '%d/%m/%Y')}).",
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())

def post_facebook_message_date(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "text": f"*BOT ILHA BABY*: Brigado {first_name}, Digite a data que você quer sair no seguinte formato DD/MM/AAAA.(Exemplo:. {datetime.date.strftime(datetime.date.today(), '%d/%m/%Y')})",
                            "quick_replies": [
                                {
                                    "content_type": "text",
                                    "title": "Data Check-out",
                                    "payload": "Check-out",
                                    "image_url": "https://www.netclipart.com/pp/m/104-1044961_calendar-icon-png-date-events-icon-white-png.png"
                                },
                            ]
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())