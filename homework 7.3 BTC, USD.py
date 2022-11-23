# Aplikacija za vremensku prognozu

import json
from urllib.request import urlopen

# moj api kljuć
api_key ="8RR0NCAPGT6SXZ7"

response = urlopen('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=' + api_key).read()

data = json.loads(response)
print(data)

print("Kratica kripto valute: " + data["Realtime Currency Exchange Rate"]["1. From_Currency Code"])

print("Naziv kripto valute: " +  data["Realtime Currency Exchange Rate"]["2. From_Currency Name"])

print("Kratica fiat valute: " + data["Realtime Currency Exchange Rate"]["3. To_Currency Code"])

print("Naziv fiat valute: " + data["Realtime Currency Exchange Rate"]["4. To_Currency Name"])

print("Tečaj kripto valute u USD : " + data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

print("Vrijeme posljednje promjene tečaja: " + data["Realtime Currency Exchange Rate"]["6. Last Refreshed"])

print("Vremenska zona : " + data["Realtime Currency Exchange Rate"]["7. Time Zone"])

print("Prodajni tečaj kripto valute u USD : " + data["Realtime Currency Exchange Rate"]["8. Bid Price"])

print("Kupovni tečaj kripto valute u USD : " + data["Realtime Currency Exchange Rate"]["9. Ask Price"])




