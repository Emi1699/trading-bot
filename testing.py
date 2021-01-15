import requests
import json
import numpy as np
# import pandas as pd

#read access tokens from external file
filepath = '../tokens.txt'
tokens = []
with open(filepath, 'r') as f:
	for line in f:
		tokens.append(line.strip())

API = "api-fxpractice.oanda.com"
STREAM_API = "stream-fxpractice.oanda.com/"

ACCESS_TOKEN = tokens[0]
ACCOUNT_ID = tokens[1]

PRICING_PATH = f"/v3/accounts/{ACCOUNT_ID}/pricing"

query = {"instruments": "EUR_USD"} 
headers = {"Authorization": "Bearer "+ ACCESS_TOKEN}

response = requests.get("https://"+API+PRICING_PATH, headers=headers, params=query)

data = response.json()

print(tokens)
print(data['prices'][0])

