import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import toks
import json
import time
import dataManipulation as dm

api = API(access_token=toks.apiToken)
params = {"instruments": "EUR_USD"}

r = pricing.PricingStream(accountID=toks.accToken, params=params)
rv = api.request(r)

maxrecs = 1
for tick in rv:
	(calendarDate, clockTime) = dm.newTime(tick['time'])
	asks = []
	bids = []

	if ('asks' in tick) and ('bids' in tick):
		for ask in tick['asks']:
			asks.append(ask['price'])

		for bid in tick['bids']:
			bids.append(bid['price'])

	askBid = zip(asks, bids)
	averages = []
	for pair in askBid:
		average = (float(pair[0]) + float(pair[1])) / 2
		averages.append(float(str(average)[:7]))

	# print(json.dumps(tick, indent=4),",")

	if tick['type'] == 'PRICE':
		print(str(tick['instrument']) + " @ " + clockTime + " -> " + str(averages) + "  " + calendarDate)
	else:
		# print(str(tick['type']) + " @ " + clockTime + " - " + calendarDate)
		print("---")

	if maxrecs == 0:
		r.terminate("maxrecs records received")

# print(rv)
# # r.response['prices'][0]
# instrumentData = rv['prices'][0]
# time = instrumentData['time']
# newTime = dm.newTime(time)

# print(str(instrumentData['instrument']) + " @ " + newTime[1] + " - " + newTime[0])

# askPrices = str(instrumentData['asks'])

# while True:
# 	print(r.response)
# 	time.sleep(0.1)

# for tick in rv:
# 	print(tick)

# for ticks in rv:
# 	print(json.dumps(rv))
# 	if maxrecs == 0:
# 		r.terminate("maxrecs records received")