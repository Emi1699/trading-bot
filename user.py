import trade
import liveDataStream

class User:
	def __init__(self, name):
		print("\nUser instantiated.\n")

		self.Trade = trade.Trade()
		self.Stream = liveDataStream.LiveDataStream("EUR_USD")
		self.name = name

	def placeTrade(self, units, instrument):
		self.Trade.placeTrade(units, instrument)
		print(self.name + " placed a trade for " + str(units) + " units in " + instrument)

	def closeTrade(self, tradeID):
		self.Trade.closeTrade(tradeID)
		print(self.name + " closed trade #" + str(tradeID))

	def closeTrades(self, tradeIDs):
		for tradeID in tradeIDs:
			self.closeTrade(tradeID)

user = User("emi")
user.placeTrade(100, "EUR_GBP")
# user.closeTrades([151, 153, 155])