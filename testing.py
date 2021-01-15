import requests
import json
import numpy as np
# import pandas as pd

API = "api-fxpractice.oanda.com"
STREAM_API = "stream-fxpractice.oanda.com/"

ACCESS_TOKEN = '**'
ACCOUNT_ID = '**'

PRICING_PATH = f"/v3/accounts/{ACCOUNT_ID}/pricing"

query = {"instruments": "EUR_USD"} 
headers = {"Authorization": "Bearer "+ ACCESS_TOKEN}

response = requests.get("https://"+API+PRICING_PATH, headers=headers, params=query)

data = response.json()

print(data['prices'][0]['type'])

