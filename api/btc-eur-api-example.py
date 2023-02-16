import requests

response = requests.get(
    "https://api.coinbase.com/v2/exchange-rates?currency=BTC"
)

responseJson = response.json()
# data = responseJson['data']
# rates = data['rates']
# btc_eur = rates['EUR']

btc_eur = responseJson['data']['rates']['EUR']

print("Valore attuale BTC EUR:")
print(btc_eur)
