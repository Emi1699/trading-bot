import trade
from liveDataStream import LiveDataStream
from commandLine import CommandLine
from fileHandler import FileHandler

class User:
	def __init__(self, name = "emi"):
		print("\nUser instantiated.\n")

		self.Trade = trade.Trade()
		self.name = name
		self.cmd = CommandLine()
		self.fileHandler = FileHandler()
		self.activeInstruments = []

		#ot = open trade
		#[OPTS] = [units, instrument]
		if self.cmd.contains("op"):
			tradeInfo = self.cmd.getOptions()
			units = tradeInfo[0]
			instrument = str(tradeInfo[1])

			if instrument == 'eurgbp':
				self.openPosition(units, "EUR_GBP")
			elif instrument == 'eurusd':
				self.openPosition(units, "EUR_USD")
			else:
				print(">--<! INVALID INSTRUMENT !>--<")

		#ops = open positions
		#[OPTS] = [units, instrument, amount]
		elif self.cmd.contains("ops"):
			tradeInfo = self.cmd.getOptions()
			units = tradeInfo[0]
			instrument = str(tradeInfo[1])
			amount = tradeInfo[2]

			if instrument == 'eurgbp':
				self.openPositions(units, "EUR_GBP", amount)
			elif instrument == 'eurusd':
				self.openPositions(units, "EUR_USD", amount)

		#ct = close trade
		#[OPTS] = [tradeID]
		elif self.cmd.contains("cp"):
			tradeInfo = self.cmd.getOptions()
			tradeID = tradeInfo[0]

			self.closeTrade(tradeID)

		#cat = close all trades
		#[OPTS] = [instrument]
		elif self.cmd.contains("cap"):
			instrument = self.cmd.getOptions()[0]
			self.closeAllTradesInstrument(instrument)

		#CAT = CLOSE ALL TRADES
		#[OPTS] = NONE
		elif self.cmd.contains("CAP"):
			self.closeAllOpenPositions()

	#open a position of x units for the desired instrument
	def openPosition(self, units, instrument):
		self.Trade.placeTrade(units, instrument)
		print(self.name + " placed a trade for " + str(units) + " units in " + instrument + "  ~~\n")

		if instrument not in self.activeInstruments:
			self.activeInstruments.append(instrument)

	def openPositions(self, units, instrument, amount):
		for _ in range(int(amount)):
			self.openPosition(units, instrument)

		# print(self.name + " placed " + str(amount) + " trades for " + str(units) + " units in " + instrument +"  ~~")

		if instrument not in self.activeInstruments:
			self.activeInstruments.append(instrument)
		print(self.activeInstruments)

	#close a single trade (soecified by its ID)
	def closeTrade(self, tradeID):
		info = self.Trade.closeTrade(tradeID)
		print(self.name + " closed trade " + info + "\n")

	#close the desired (specified by argument) trades
	def closeTrades(self, tradeIDs):
		for tradeID in tradeIDs:
			self.closeTrade(tradeID)

	#stream live quotes for the chosen currency pair
	def streamLiveQuotes(self, currencyPairs):
		stream = LiveDataStream(currencyPairs)
		stream.streamData()

	#return list with ids of all currently open trades
	def getOpenPositions(self, instrument):
		#get open trades' ids
		openTrades = []
		with open('open trades/' + instrument, 'r') as f:
		    for line in f:
		    	openTrades.append(line[:4])

		return openTrades

	#close all open positions for a given instrument
	def closeAllTradesInstrument(self, instrument):
		for tradeID in self.getOpenPositions(instrument):
			self.closeTrade(int(tradeID[-3:]))

		print("All positions in " + instrument + " have been closed.\n")

	#### !!!!!! WORK IN PROGRESS !!! ############################
	#close ALL open positions (for all instruments)
	def closeAllOpenPositions(self):
		for instrument in self.activeInstruments:
			if not self.fileHandler.isEmpty(instrument):
				self.closeAllTradesIn(instrument)

		print("CLOSED ALL OPEN POSITIONS!\n")

user = User("Emi")
# user.streamLiveQuotes("EUR_GBP,EUR_USD")
user.openPosition(100, "EUR_GBP")
# user.closeTrades([191])
