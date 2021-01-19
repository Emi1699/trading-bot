import trade

class User:
	def __init__(self):
		print("\nUser instantiated.\n")

		self.Trade = trade.Trade()

	def placeTrade(self, units, instrument):
		self.Trade.placeTrade(units, instrument)

	def closeTrade(self, tradeID):
		self.Trade.closeTrade(tradeID)

	