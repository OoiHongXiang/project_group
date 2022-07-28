import requests

def api():
    api_key = "CD3X4CGU9YGHWX5S"
    url =  f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

    response = requests.get(url)
    data = response.json()
    
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return(rate)

print(api())