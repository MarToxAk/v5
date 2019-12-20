from ..models import CotaçõesModels, Valor_CotaçãoModels, PousadaModels
import requests
from bs4 import BeautifulSoup



def CotaçõesServiços(cotações):
    cotação2 = CotaçõesModels(checkin=cotações.checkin, checkout=cotações.checkout, num_adultos=cotações.num_adultos, num_crianças=cotações.num_crianças, user=cotações.user)
    cotação2.save()
    cotação2.pousadas.set(cotações.pousadas)
    cotação2.save()

    def valor_da_cotações():
        for queryset in cotação2.pousadas.all():
            pousada = PousadaModels.objects.get(id=queryset.id)
            linkp = queryset.link
            headers = {
                'host': 'www.booking.com',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
            }

            payload = {'checkin': cotações.checkin, 'checkou': cotações.checkout, 'group_adults': cotações.num_adultos,
                       'group_children': cotações.num_crianças}

            # Use the object above to connect to needed webpage
            resp = requests.get(
                f"https://www.booking.com/hotel/br/{linkp}.html?aid=1258472&checkin={cotações.checkin}&checkout={cotações.checkout}&dest_id=-646567&dest_type=city&group_adults={cotações.num_adultos}&group_children={cotações.num_crianças}",
                headers=headers, params=payload)

            try:
                soup = BeautifulSoup(resp.content, "lxml")
                option_tags = soup.find_all("div", {"class": "bui-price-display__value"})
                preco = option_tags[0].get_text()
                valor = preco[3:].replace('.', '')
                valor = float(valor)
            except Exception:
                valor = float(0.00)

            valor_cotação = Valor_CotaçãoModels(nome=str(f'{cotações.checkin} á {cotações.checkout}'),
                                                valor=valor, user=cotações.user, cotacao=pousada)
            valor_cotação.save()
            cotação2.valor.add(valor_cotação)
            
            


    valor_da_cotações()


def update_cotação(cotações):
    update_cot = CotaçõesModels.objects.filter(pk=cotações.id)
    update_cot.update(checkin=cotações.checkin, checkout=cotações.checkout, num_adultos=cotações.num_adultos, num_crianças=cotações.num_crianças, user=cotações.user)
    update_cot = CotaçõesModels.objects.get(pk=cotações.id)
    update_cot.pousadas.set(cotações.pousadas)
    
    def valor_da_cotações():
        valor_queryset = ()
        for queryset in update_cot.pousadas.all():
            pousada = PousadaModels.objects.get(id=queryset.id)
            linkp = queryset.link
            headers = {
                'host': 'www.booking.com',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
            }

            payload = {'checkin': cotações.checkin, 'checkou': cotações.checkout, 'group_adults': cotações.num_adultos,
                       'group_children': cotações.num_crianças}

            # Use the object above to connect to needed webpage
            resp = requests.get(
                f"https://www.booking.com/hotel/br/{linkp}.html?aid=1258472&checkin={cotações.checkin}&checkout={cotações.checkout}&dest_id=-646567&dest_type=city&group_adults={cotações.num_adultos}&group_children={cotações.num_crianças}",
                headers=headers, params=payload)

            try:
                soup = BeautifulSoup(resp.content, "lxml")
                option_tags = soup.find_all("div", {"class": "bui-price-display__value"})
                preco = option_tags[0].get_text()
                valor = preco[3:].replace('.', '')
                valor = float(valor)
            except Exception:
                valor = float(0.00)

            valor_cotação = Valor_CotaçãoModels(nome=str(f'{cotações.checkin} á {cotações.checkout}'),
                                                valor=valor, user=cotações.user, cotacao=pousada)
            valor_cotação.save()
            valor_queryset = valor_queryset + (valor_cotação.id,)
            
        
        test = Valor_CotaçãoModels.objects.filter(id__in=valor_queryset)            
        update_cot.valor.set(test)
    valor_da_cotações()