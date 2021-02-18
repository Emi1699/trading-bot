import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import json
from oandapyV20 import API
import toks
import fileHandler as fh

class Trade():
	def __init__(self, apiToken = toks.AccessTokens().apiToken(), accToken = toks.AccessTokens().accToken()):
		# print("\n Trade Object created.\n")

		self.apiToken = apiToken
		self.accToken = accToken
		self.api = API(access_token = self.apiToken)
		self.fileHandler = fh.FileHandler()

	def placeTrade(self, units, instrument):
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
		# print("processing : {}".format(r))
		# print("===============================")
		# print(r.data)
		try:
			response = self.api.request(r)

			#get some basic info about the trade we placed
			openedTradeId = str(response['orderFillTransaction']['tradeOpened']['tradeID'])
			price = str(response['orderFillTransaction']['tradeOpened']['price'])
			units = str(response['orderFillTransaction']['tradeOpened']['units'])
			instrument = str(response['orderFillTransaction']['instrument'])

			#add basic info to the specific file in the 'open trades' directory
			fileEntry = "#" + openedTradeId + ' -> ' + units + " units @ " + price + "   ~~"
			self.fileHandler.newEntry_tradePlaced(instrument, fileEntry)

		except V20Error as e:
			print("V20Error: {}".format(e))
		# else:
		# 	print("Response: {}\n{}".format(r.status_code, json.dumps(response, indent=2)))

	def closeTrade(self, trade_id):
		r = trades.TradeClose(self.accToken, tradeID = str(trade_id))
		response = self.api.request(r)

		closedTradeId = str(response['orderFillTransaction']['tradesClosed'][0]['tradeID'])
		closingPrice = str(response['orderFillTransaction']['tradesClosed'][0]['price'])
		# units = str(response['orderFillTransaction']['tradesClosed']['units'])
		instrument = str(response['orderFillTransaction']['instrument'])
		realizedPL = str(response['orderFillTransaction']['tradesClosed'][0]['realizedPL'])

		# print("RESP:\n{} ".format(json.dumps(response, indent=2)))

		#remove trade from 'open trades' directory
		self.fileHandler.removeEntry_trade(trade_id, instrument)

		#add new entry in the 'closed trades' directory
		content = "#" + closedTradeId + " @ " + closingPrice + " // PL: " + realizedPL + "   ~~"
		self.fileHandler.newEntry_tradeClosed(instrument, content)

		return content

trade = Trade()

trade.placeTrade(1000, "EUR_GBP")
# trade.closeTrade(134)
# trade.closeTrade(137)




