import requests
import json


exchanges = {
    'доллар': 'RUB_USD',
    #'евро': 'EUR',
    'рубль': 'USD_RUB'
}

TOKEN = "5190770347:AAG2UzUtbOzqlWXc4aYoFUW72kk16tTnvmY"

base_key = 'USD_RUB'
sym_key = 'RUB_USD'
amount = 100


r = requests.get(f"https://free.currconv.com/api/v7/convert?q={base_key},{sym_key}&compact=ultra&apiKey=2f98ff25fe53cb6c6e61")

resp = json.loads(r.content)
new_price = resp[sym_key] * amount
print(new_price)