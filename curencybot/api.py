import requests
import json

base_key = 'USD'
sym_key = 'RUB'
amount = 100


r = requests.get(f"https://free.currconv.com/api/v7/convert?q=USD_RUB,RUB_USD&compact=ultra&apiKey=2f98ff25fe53cb6c6e61")

resp = json.loads(r.content)
new_price = resp[sym_key] * amount
print(new_price)