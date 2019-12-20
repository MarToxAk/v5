import requests
from bs4 import BeautifulSoup
num = 0
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
    img = soup2.find('meta', property='og:image')
    img = img['content']
    print(img)
    num = num + 1
    img_data = requests.get(img).content
    try:
        with open(f'{num}{nome.strip()}.jpg', 'wb') as handler:
            handler.write(img_data)
    except Exception:
        pass