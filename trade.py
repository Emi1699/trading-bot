import oandapyV20.endpoints.orders as orders
import json
from oandapyV20 import API
import toks
import fileHandler as fh

class Trade():
	def __init__(self, apiToken = toks.AccessTokens().apiToken(), accToken = toks.AccessTokens().accToken()):
		print("\n Trade Object created.\n")

		self.apiToken = apiToken
		self.accToken = accToken
		self.api = API(access_token = self.apiToken)
		self.fileHandler = fh.FileHandler()

	def marketOrder(self, units, instrument):
		orderConf = {
	         "order": {
	            "units": str(units),
	            "instrument": instrument,
	            "timeInForce": "IOC",
	            "type": "MARKET",
	            "positionFill": "DEFAULT"
	          }
	        }

		r = orders.OrderCreate(accountID = self.accToken, data = orderConf)
		print("processing : {}".format(r))
		print("===============================")
		print(r.data)
		try:
			response = self.api.request(r)
			
			transactionID = str(response['orderFillTransaction']['tradeOpened']['tradeID'])
			price = str(response['orderFillTransaction']['tradeOpened']['price'])
			units = str(response['orderFillTransaction']['tradeOpened']['units'])
			instrument = str(response['orderFillTransaction']['instrument'])

			self.fileHandler.newEntryTradePlaced(instrument, "#" + transactionID + ' -> ' + units + " units @ " + price + "   ~~")

		except V20Error as e:
			print("V20Error: {}".format(e))
		else:
			print("Response: {}\n{}".format(r.status_code, json.dumps(response, indent=2)))

trade = Trade()

trade.marketOrder(1000, "EUR_USD")