# Import the requests library 
import requests 
  
# Define endpoint 
endpoint = "https://api.taapi.io/bulk"
  
# Define a JSON body with parameters to be sent to the API 
parameters = {
    "secret": "",
    "construct": {
        "exchange": "binance",
        "symbol": "BTC/USDT",
        "interval": "1h",
        "indicators": [
	    {
                # Relative Strength Index
	        "indicator": "rsi"
	    },
            {
                
	        "indicator": "avgprice"
	        
	    },
	  
        ]
    }
}
  
# Send POST request and save the response as response object 
response = requests.post(url = endpoint, json = parameters)
  
# Extract data in json format 
result = response.json() 

# Print result
print(result)