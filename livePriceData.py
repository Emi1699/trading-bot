import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import toks
import json
import time

api = API(access_token=toks.apiToken)
params = {"instruments": "EUR_USD"}

r = pricing.PricingInfo(accountID=toks.accToken, params=params)
rv = api.request(r)

print(str(r.response['prices'][0]['instrument'])

# while True:
# 	print(r.response)
# 	time.sleep(0.1)

# for tick in rv:
# 	print(tick)

# for ticks in rv:
# 	print(json.dumps(rv))
# 	if maxrecs == 0:
# 		r.terminate("maxrecs records received")