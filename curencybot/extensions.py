import requests
import json
from config import exchanges

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            return APIException(f"Валюта {base} не найдена")
        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена")
        if base_key == sym_key:
            raise APIException(f"Невозможно перевести одинаковые валюты{base}")
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")

        r = requests.get(f"http://api.currencylayer.com/live?access_key=cf0b7a82426dee5db479c1bec14250f8")
        resp = json.loads(r.content)
        new_price = resp['quotes']['USDRUB'] * float(amount)
        return round(new_price, 2)
