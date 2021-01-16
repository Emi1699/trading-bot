import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import toks
import json
import time
import dataManipulation as dm

api = API(access_token=toks.apiToken)
params = {"instruments": "EUR_USD"}

r = pricing.PricingInfo(accountID=toks.accToken, params=params)
rv = api.request(r)

instrumentData = r.response['prices'][0]
time = instrumentData['time']
newTime = dm.newTime(time)

print(str(instrumentData['instrument']) + " @ " + newTime[1] + " - " + newTime[0])

askPrices = str(instrumentData['asks'])

# while True:
# 	print(r.response)
# 	time.sleep(0.1)

# for tick in rv:
# 	print(tick)

# for ticks in rv:
# 	print(json.dumps(rv))
# 	if maxrecs == 0:
# 		r.terminate("maxrecs records received")