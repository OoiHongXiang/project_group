import requests

def api():
    """
    This function makes an API call to alphavantage.co to extract the real time exchange rate (Forex) from USD to SGD.
    """
    
    api_key = "CD3X4CGU9YGHWX5S"
    url =  f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    # url for currency exchange rate from USD to SGD with API key is assigned to url variable.

    response = requests.get(url)
    # request access to the url
    data = response.json()
    # retrieve data with .json from response and save it as data
    
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    # extracts Real Time Currency Exchange Rate from data and converts into float for easy multiplication later on, assigned to rate variable
    return(rate)
    # returns the rate extracted from the data

print(api())