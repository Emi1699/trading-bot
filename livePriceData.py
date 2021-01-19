import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import toks
import json
import time
import dataManipulation as dm
import fileHandler as fh

class LiveDataStream():
	def __init__(self, currencyPairs):
		print("\nliveDataStream Object created.\n")

		self.fileHandler = fh.fileHandler()
		self.currencyPairs = currencyPairs

	def connect(self):
		api = API(access_token = toks.apiToken)
		params = {"instruments": self.currencyPairs}

		r = pricing.PricingStream(accountID = toks.accToken, params = params)

		return api.request(r)

	def streamData(self):
		rv = self.connect()
		# maxrecs = 1
		for tick in rv:
			(calendarDate, clockTime) = dm.formattedTime(tick['time'])
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
				askBidDifference = (float(pair[0]) + float(pair[1])) / 2
				averages.append(askBidDifference)

			if tick['type'] == 'PRICE':
				currencyPair = tick['instrument']
				average = str(sum(averages) / len(averages))[:7]

				self.fileHandler.newEntry(currencyPair, str(average) + ", " + str(clockTime) + ", " + str(calendarDate))
				print(currencyPair + " @ " + clockTime + " -> " + str(average) + "  " + calendarDate)
			else:
				# print(str(tick['type']) + " @ " + clockTime + " - " + calendarDate)
				print("---")

			# if maxrecs == 0:
			# 	r.terminate("maxrecs records received")

	def getStreamingCurrencyPairs(self):
		return self.currencyPairs.split(',')


liveStream = LiveDataStream("EUR_USD,EUR_GBP")
liveStream.streamData()
print(liveStream.getStreamingCurrencyPairs())




