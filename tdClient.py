from twelvedata import TDClient
import toks
from datetime import datetime
from today import Today

class ForexData():
	today = Today().datetime()

	def __init__(self, currencyPair, interval, endDate, output = 1):
		self.client = TDClient(toks.AccessTokens().TDtoken())
		self.technicalIndicators = ["bbands", "rsi", "macd", "stoch"]
		self.currencyPair = currencyPair
		# self.startDate = startDate
		self.endDate = endDate
		self.interval = interval
		self.output = output

	def getPriceData(self):
		ts = self.client.time_series(
		    symbol = self.currencyPair,
		    outputsize = self.output,
		    interval = self.interval,
		    # start_date = self.startDate,
		    end_date = self.endDate,
		    timezone = "Europe/Bucharest"
		)

		return ts

	def getDataWithIndicators(self):
		ts = self.getPriceData()
		if "bbands" in self.technicalIndicators:
			ts = ts.with_bbands()
		if "macd" in self.technicalIndicators:
			ts = ts.with_macd()
		if "rsi" in self.technicalIndicators:
			ts = ts.with_rsi()
		if "ichimoku" in self.technicalIndicators:
			ts = ts.with_ichimoku()
		if "stoch" in self.technicalIndicators:
			ts = ts.with_stoch()
		if "ma" in self.technicalIndicators:
			ts = ts.with_ma()

		return ts

	def setInterval(self, interval):
		self.interval = interval

	def setTechnicalIndicators(self, indicators):
		self.technicalIndicators = indicators.split(' ')


def strToTime(time):
	return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

today = ForexData.today

# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

endDate = strToTime(str("2020-07-15 12:36:00"))
interval = 1
dataPoints = 5000


while True:
	data = ForexData("EUR/USD", str(interval) + "min", endDate, dataPoints)
	dtt = data.getDataWithIndicators().as_pandas()
	dtt.to_csv("price data/emi.csv", float_format='%.5f', mode = 'a', header = False)

	endDate = strToTime(str(dtt.index[dataPoints - 1]))


