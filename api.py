import requests
import json

base_key = 'USD'
sym_key = 'RUB'
amount = 100


r = requests.get(f"http://api.currencylayer.com/live?access_key=cf0b7a82426dee5db479c1bec14250f8")

resp = json.loads(r.content)
new_price = resp['quotes']['USDRUB'] * amount
print(new_price)