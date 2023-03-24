import requests
import json

def AV_Query(symbol, function):
    apikey = "T6IGSBW0GEMTVTMA"
    url = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + symbol + '&apikey=' + apikey
    r = requests.get(url)
    data = r.json()
    return data

def menu():
    stocksymbol = input("Enter the stock symbol: ")
    charttype = input("Enter the chart type: ")
    function = input("Enter the time series function: ")
    startdate = input("Enter the beginning date in YYYY-MM-DD format: ")
    enddate = input("Enter the end date in YYYY-MM-DD format: ")
        
   
   
    
def main():
    menu()
    data = AV_Query("I", "TIME_SERIES_MONTHLY_ADJUSTED")
    print(data)
  
main()
    