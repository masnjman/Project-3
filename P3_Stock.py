import requests
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

# Alpha Vantage API URL
url = "https://www.alphavantage.co/query"

# Alpha Vantage API key
api_key = "T6IGSBW0GEMTVTMA"

# User input prompts
symbol = input("Enter stock symbol: ")
chart_type = input("Enter chart type (line, bar, or scatter): ")
function = input("Enter time series function (daily, weekly, monthly, etc.): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# API parameters
params = {
    "function": function,
    "symbol": symbol,
    "apikey": api_key
}

# Get the data from the API
response = requests.get(url, params=params)
data = response.json()

# Convert data to pandas DataFrame
df = pd.DataFrame.from_dict(data[f"Time Series ({function})"], orient="index")

# Convert date strings to datetime objects
df.index = pd.to_datetime(df.index)

# Filter the data by date range
df = df.loc[start_date:end_date]

# Generate the chart
if chart_type == "line":
    plt.plot(df)
elif chart_type == "bar":
    plt.bar(df.index, df["4. close"])
elif chart_type == "scatter":
    plt.scatter(df.index, df["4. close"])

# Add chart title and labels
plt.title(f"{symbol} Stock Prices ({function})")
plt.xlabel("Date")
plt.ylabel("Price")

# Display the chart
plt.show()

# Open chart in default browser
webbrowser.open_new_tab("file:///" + "/".join(plt.savefig("chart.png").split("\\")[1:]))
