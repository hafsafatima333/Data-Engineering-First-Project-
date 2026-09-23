# import requests

# response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
# price = response.json()["quotes"]["USD"]["price"]
# print(price)


import requests
import json
response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
data = response.json()


formatted_data = json.dumps(data, indent = 4)
print("Formatted data")
print(formatted_data)


print("\n" + "="*50 + "\n")

market_cap_change_24h= data["quotes"] ["USD"] ["market_cap_change_24h"]
print("Market Cap Change 24h: ", market_cap_change_24h)

price = data["quotes"]["USD"]["price"]
print("Price: ", price)
