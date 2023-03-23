import requests

def av_query(symbol, function):
    apikey = "T6IGSBW0GEMTVTMA"
    url = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + symbol + '&apikey=' + apikey
    r = requests.get(url)
    data = r.json()
    return data
    
    
def main():
    data = av_query("IBM", "TIME_SERIES_MONTHLY_ADJUSTED")
    print(data)
    
main()
    