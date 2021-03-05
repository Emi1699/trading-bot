from twelvedata import TDClient
import toks
from datetime import datetime, timedelta
from today import Today
import time
from fileHandler import FileHandler

class ForexData():
	today = Today().datetime()

	def __init__(self, currencyPair, interval, endDate, output = 1):
		self.client = TDClient(toks.AccessTokens().TDtoken())
		self.technicalIndicators = ['ma', "bbands", "rsi", "wma"]
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
		#time periods over which indicators are computed are numbers from the fibonacci sequence
		ts = self.getPriceData()
		# TREND
		if "ma" in self.technicalIndicators:
			ts = ts.with_ma(time_period = 3).with_ma(time_period=5).with_ma(time_period=8).with_ma(time_period=13).with_ma(time_period=21)
		if "wma" in self.technicalIndicators:
			ts = ts.with_wma(time_period = 3).with_wma(time_period=5).with_wma(time_period=8).with_wma(time_period=13).with_wma(time_period=21)
		# VOLATILITY
		if "bbands" in self.technicalIndicators:
			ts = ts.with_bbands(time_period = 3).with_bbands(time_period=5).with_bbands(time_period=8).with_bbands(time_period=13).with_bbands(time_period=21)
		# MOMENTUM
		if "rsi" in self.technicalIndicators:
			ts = ts.with_rsi(time_period = 3).with_rsi(time_period=5).with_rsi(time_period=8).with_rsi(time_period=13).with_rsi(time_period=21)

		# VOLUME IS HARD TO CALCULATE FOR FOREX PAIRS, BECAUSE THE MARKET IS
		#HIGHLY DECENTRALIZED AND EXTREMELY VOLATILE

		return ts

	def setInterval(self, interval):
		self.interval = interval

	def setTechnicalIndicators(self, indicators):
		self.technicalIndicators = indicators.split(' ')

def strToTime(time):
	return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

endDate = Today().datetime()
print("last time: " + str(endDate))

#get a times * 5000 datapoints in the corresponding pair file file
def getBatchToFiles(pair, interval, dataPoints, endDate, times = 4):
	for _ in range(times):
		print("requesting " + str(pair) + "...")
		data = ForexData(pair, str(interval) + "min", endDate, dataPoints)
		dtt = data.getDataWithIndicators().as_pandas()

		print("adding to file...")
		dtt.to_csv("price data/" + pair[:3] + "_" + pair[4:], float_format='%.5f', mode = 'a', header = False)

		print("computing next end date...")
		endDate = strToTime(str(dtt.index[dataPoints - 1])) - timedelta(minutes=interval)
		print("Done. Waiting for next batch...\n\n")
		time.sleep(15)

forexPairs = ["USD/EUR", "USD/JPY", "GBP/USD", "EUR/GBP", "EUR/USD"]
interval = 15 #minutes interval  (e.g. 1min, 10min, 15min, etc)
dataPoints = 5000

for pair in forexPairs:
	FileHandler().writeToFile("price data/" + str(interval) + "min/" + pair[:3] + "_" + pair[4:], "datetime,open,high,low,close,ma1,ma2,ma3,ma4,ma5,wma1,wma2,wma3,wma4,wma5,upper_band1,middle_band1,lower_band1,upper_band2,middle_band2,lower_band2,upper_band3,middle_band3,lower_band3,upper_band4,middle_band4,lower_band4,upper_band5,middle_band5,lower_band5,rsi1,rsi2,rsi3,rsi4,rsi5")
	getBatchToFiles(pair, interval, dataPoints, endDate)

# emi = "usd/jpy"
# print(emi[:3] + "_" + emi[4:])
# print(datetime.strptime('2018-06-29 08:15:27', '%Y-%m-%d %H:%M:%S' ) + timedelta(minutes=13))
# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
