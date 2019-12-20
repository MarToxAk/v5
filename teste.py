import requests
from bs4 import BeautifulSoup
import json
import short_url

link_produto = {}
headers = {
    'host': 'www.follyprontaentrega.com.br',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

resp = requests.get(
                f"https://www.follyprontaentrega.com.br/search.html",
                headers=headers)

soup = BeautifulSoup(resp.content, "lxml")
option_tags = soup.find_all("div", {"class": "product-item-container"})
for teste in option_tags:
    tamanholist = []
    link = teste.find("div", {"class": "iluria-layout-search-product-title"}).find('a')
    nome = teste.find("div", {"class": "iluria-layout-search-product-title"}).find('a').text
    t = f"https://www.follyprontaentrega.com.br/{link['href']}"
    resp2 = requests.get(f"{t}", headers=headers)
    soup2 = BeautifulSoup(resp2.content, "lxml")
    #print(soup2)
    img = soup2.find('meta', property='og:image')
    img = img['content']
    preço = soup2.find('div', {'class': 'iluria-product-price'}).find('span', {'class': 'product-price-text'}).text
    preço = float(f'{preço}'.replace(',', '.'))
    tamanho = soup2.find('div', {'class': 'product-variations-container'}).find('select', {'id': 'iluria-product-variation1'})
    for tamanho in tamanho.find_all('option', {'class': 'variation1-option'}):
        tamanho2 = tamanho.text.strip()
        tamanholist.append(tamanho2)

    if len(tamanholist) == 5:
        textamanho = f'{tamanholist[0]} {tamanholist[1]} {tamanholist[2]} {tamanholist[3]} {tamanholist[4]}'
    elif len(tamanholist) == 4:
        textamanho = f'{tamanholist[0]} {tamanholist[1]} {tamanholist[2]} {tamanholist[3]}'
    elif len(tamanholist) == 3:
        textamanho = f'{tamanholist[0]} {tamanholist[1]} {tamanholist[2]}'
    elif len(tamanholist) == 2:
        textamanho = f'{tamanholist[0]} {tamanholist[1]} '
    elif len(tamanholist) == 1:
        textamanho = f'{tamanholist[0]}'
    else:
        textamanho = f'Não disponivel'
    compra = f'Oi Fiquei interessado(a) nesse produto {nome.strip()} - Tamanho {textamanho} - Encomenda'.replace(' ','%20')
    link_compra = f'https://api.whatsapp.com/send?phone=5512996745251&text={compra}'
    linkRequest = {
        "destination": link_compra
        , "domain": {"fullName": "rebrand.ly"}
        # , "slashtag": "A_NEW_SLASHTAG"
        # , "title": "Rebrandly YouTube channel"
    }

    requestHeaders = {
        "Content-type": "application/json",
        "apikey": "6084b8f72b1b49cbb37ceaadb68972c2",
        "workspace": ""
    }

    r = requests.post("https://api.rebrandly.com/v1/links",
                      data=json.dumps(linkRequest),
                      headers=requestHeaders)

    if (r.status_code == requests.codes.ok):
        link = r.json()
        wpp_short = f"http://{link['shortUrl']}"

    id = nome.strip().replace(' ', '-')
    nome = f"{nome.strip()} - Encomenda"
    preço = (preço*175)/100+preço
    if preço >= 53:
        preço = 54.99
    elif preço >= 19 and preço <= 29.4:
        preço = 19.99
    elif preço <= 41 and preço >= 31.6:
        preço = 34.99
    elif preço <= 31.5 and preço >= 29.5:
        preço = 29.99
    else:
        preço = 999.99

    descrição = f"Tamanho Disponível {textamanho} . Temos novas remessas toda sexta-feira. Nosso prazo para entrega é de 5 a 10 dias. Frete grátis para produtos escrito 'Encomenda'. O Link de Compra vai redireciona-los para o WhatsApp da loja para que sejam atendidos pela nossa equipe."
    print(f'{id},{nome},{descrição},in stock,New,{preço:.2f},{wpp_short},{img},Facebook,Clothing & Accessories> Clothing')