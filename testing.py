import requests
import json
import numpy as np

# import sys
# sys.path.insert(1, '/oanda-api-v20')

from oandapyV20 import API
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.positions as positions
# import pandas as pd

#read access tokens from external file
filepath = '/Users/emi_buliga/Desktop/tokens.txt'
tokens = []
with open(filepath, 'r') as f:
	for line in f:
		tokens.append(line.strip())

apiToken = tokens[0]
accToken = tokens[1]

REST_API = "api-fxpractice.oanda.com"
STREAM_API = "stream-fxpractice.oanda.com/"

ACCESS_TOKEN = apiToken
ACCOUNT_ID = accToken

PRICING_PATH = f"/v3/accounts/{ACCOUNT_ID}/pricing"

query = {"instruments": "Gold"} 
headers = {"Authorization": "Bearer "+ ACCESS_TOKEN}

response = requests.get("https://"+REST_API+PRICING_PATH, headers=headers, params=query)

data = response.json()

# print(data)

# for el in data['prices'][0]:
# 	print(str(el) + " -> " + str(data['prices'][0][el]) + "\n")

# get a list of trades

#get trade history
api = API(access_token = apiToken)
accountID = accToken

r = trades.TradesList(accountID)
# show the endpoint as it is constructed for this call
print("REQUEST:{}".format(r))
rv = api.request(r)
print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))

r = positions.OpenPositions(accountID=accountID)
openPos = api.request(r)

for pos in openPos:
	print(openPos)

