import requests

def av_query(symbol, function):
    apikey = "T6IGSBW0GEMTVTMA"
    url = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + symbol + '&apikey=' + apikey
    r = requests.get(url)
    data = r.json()
    return data
    
def get_chart_type():
    print("Chart Types")
    print("-----------")
    print("1. Bar \n2. Line\n")
    while(True):
        try:
            chart_type = int(input("Enter the chart type you want (1, 2):"))
            if chart_type < 1 or chart_type > 2:
                print("please enter only a 1 or a 2")
                continue
        except Exception as err:
            print(err)
        else:
            break
    return chart_type

def get_time_series():
    print("Select the Time series of the chart you want to Generate")
    print("--------------------------------------------------------")
    print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    while(True):
        try:
            choice = int(input("Enter time series option (1, 2, 3, 4): "))
            if choice < 1 or choice > 4:
                print("please enter only a 1, 2, 3, or 4")
                continue
        except Exception as err:
            print(err)
        else:
            break
    if choice == 1:
        time_series = "TIME_SERIES_INTRADAY_ADJUSTED"
    elif choice == 2:
        time_series = "TIME_SERIES_DAILY_ADJUSTED"
    elif choice == 3:
        time_series = "TIME_SERIES_WEEKLY_ADJUSTED"
    else:
        time_series = "TIME_SERIES_MONTHLY_ADJUSTED"
    return time_series

def bar_chart():
    return

def line_chart():
    return

def main():
    data = av_query("IBM", "TIME_SERIES_MONTHLY_ADJUSTED")
    
    
    print("Stock Data Visualizer")
    print("---------------------")
    stock_symbol = input("Enter the stock symbol you are looing for: ")
    chart_type = get_chart_type()
    time_series = get_time_series()
    start_date = input("Enter the start Date (YYYY-MM-DD): ")
    end_date = input("Enter the start Date (YYYY-MM-DD): ")

    mydata = av_query(stock_symbol, time_series)
    
    print()


    if chart_type == 1:
        bar_chart(the_data)
    else:
        line_chart(the_data)



    
main()
    