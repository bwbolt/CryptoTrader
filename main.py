import schedule
import time
import robin_stocks
import robin_stocks.robinhood as r
from buyText import *
from sellText import *


# This if for logging into Robinhood via the robinstocks api
# currently im going to keep this commented out untill I do more testing

# def login():
#  r.login(###, ###)

# login()
#print("You are now logged into robinhood... scanning for trading opportunity")


def theJob():

    # Import the requests library
    import requests

# Define endpoint
    endpoint = "https://api.taapi.io/bulk"

# Define a JSON body with parameters to be sent to the API
    parameters = {
        "secret": "###",
        "construct": {
            "exchange": "binance",
            "symbol": "ETH/USDT",
            "interval": "1m",
            "indicators": [
                {

                  "indicator": "rsi"
                },
                {

                    "indicator": "avgprice"

                },
                {

                    "indicator": "dmi"

                },
                {

                    "indicator": "macd"

                },


            ]
        }
    }

# Send POST request and save the response as response object
    response = requests.post(url=endpoint, json=parameters)

# Extract data in json format
    result = response.json()


# Price from result
    price = result["data"][1]["result"]["value"]

# RSI Value from result
    rsi = result["data"][0]["result"]["value"]


# DMI from results
    dmi = result["data"][2]["result"]["adx"]

# MacD from results
    macd = result["data"][3]["result"]["valueMACD"]


# variable for price at buy
    boughtAt = 0

# Print result

    print(price)
    print(macd)
    print(rsi)
    print(dmi)
    print(boughtAt)
    print("-------------------------------------------------")

    if macd < -6 and rsi < 30 and dmi > 39:
        print("time to buy!!!!!")
        boughtAt = price
        buyText()

    if macd > 6 and rsi > 70 and dmi > 23 and price > boughtAt:
        print("time to sell!!!!!")
        boughtAt = 0
        sellText()


# running theJob every 15 seconds
schedule.every(.25).minutes.do(theJob)

while True:
    schedule.run_pending()
    time.sleep(1)



#will be adding automation down here




