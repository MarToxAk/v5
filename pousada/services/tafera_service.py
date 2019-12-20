from ..models import CasadePedraCotacao
from bs4 import BeautifulSoup
import requests


def cadastra_cotação(cotação):
    CasadePedraCotacao.objects.create(author=cotação.author, name=cotação.name, tel=cotação.tel, checkin=cotação.checkin,
                                      checkout=cotação.checkout, person_num=cotação.person_num, kidquestion=cotação.kidquestion, kid1=cotação.kid1,
                                      kid2=cotação.kid2, kid3=cotação.kid3, discount=cotação.discount, dialy_of_price=cotação.dialy_of_price,
                                      portion=cotação.portion)


def webdrive(checkin, checkout, person_num, kidquestion, kid1, kid2, kid3):

    headers = {
        'Host': 'reservations.omnibees.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers'
    }
    bot = requests.session()
    r = bot.get(
        f'https://reservations.omnibees.com/default.aspx?q=3661',
        headers=headers)
    soup2 = BeautifulSoup(r.content, "lxml")
    sid = soup2.find("input", {"id": "hfSID"}).get('value')

    resp = bot.get(
        f"https://reservations.omnibees.com/Handlers/ajaxLoader.ashx?ucUrl=SearchResultsByRoom&&diff=false&CheckIn={checkin}&CheckOut={checkout}&Code=&group_code=&loyality_card=&NRooms=1&ad={person_num}&ch={kidquestion}&ag={'' if kid1 == None else kid1}{ '' if kid2 == None else ';'+str(kid2)}{ '' if kid3 == None else ';'+str(kid3)}&q=3661&sid={sid}",
        headers=headers)

    try:
        soup = BeautifulSoup(resp.content, "lxml")
        restricao = soup.find_all("span", {"class": "divInfo"})
        texto_restricao = option_tags[0].get_text()
        if texto_restricao == 'Verifique as Restrições do Tarifário':
            Valor = 0.0
        else:
            option_tags = soup.find_all("a", {"class": "price_tooltip"})
            preco = option_tags[0].get_text()
            valor = preco[3:].replace(',', '.')
            valor = float(valor)
    except Exception:
        valor = float(0.00)

    return valor
