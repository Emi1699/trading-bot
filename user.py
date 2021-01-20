import trade
from liveDataStream import LiveDataStream
from commandLine import CommandLine

class User:
	def __init__(self, name = "emi"):
		print("\nUser instantiated.\n")

		self.Trade = trade.Trade()
		self.Stream = LiveDataStream("EUR_USD")
		self.name = name
		self.cmd = CommandLine()

		if self.cmd.contains("ot"):
			tradeInfo = self.cmd.getOptions()
			units = tradeInfo[0]
			instrument = str(tradeInfo[1])

			if instrument == 'eg':
				self.placeTrade(units, "EUR_GBP")
			elif instrument == 'eu':
				self.placeTrade(units, "EUR_USD")
				
		elif self.cmd.contains("ct"):
			tradeInfo = self.cmd.getOptions()
			tradeID = tradeInfo[0]

			self.closeTrade(tradeID)

	def placeTrade(self, units, instrument):
		self.Trade.placeTrade(units, instrument)
		print(self.name + " placed a trade for " + str(units) + " units in " + instrument)

	def closeTrade(self, tradeID):
		info = self.Trade.closeTrade(tradeID)
		print(self.name + " closed trade " + info)

	def closeTrades(self, tradeIDs):
		for tradeID in tradeIDs:
			self.closeTrade(tradeID)

user = User("emi")
# user.placeTrade(100, "EUR_GBP")
# user.closeTrades([191])