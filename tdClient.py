from twelvedata import TDClient
import toks
from datetime import datetime


class ForexData():
	today = datetime.today().strftime('%Y-%m-%d')

	def __init__(self, currencyPair, interval, endDate, output = 1, startDate = "1901-01-01"):
		self.client = TDClient(toks.AccessTokens().TDtoken())
		self.technicalIndicators = ["bbands", "rsi"]
		self.currencyPair = currencyPair
		self.startDate = startDate
		self.endDate = endDate
		self.interval = interval
		self.output = output

	def getPriceData(self):
		ts = self.client.time_series(
		    symbol = self.currencyPair,
		    outputsize = self.output,
		    interval = self.interval,
		    start_date = self.startDate,
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
		if "macd" in self.technicalIndicators:
			ts = ts.with_macd()
		if "ichimoku" in self.technicalIndicators:
			ts = ts.with_ichimoku()

		return ts.as_pandas()

	def setInterval(self, interval):
		self.interval = interval

	def setTechnicalIndicators(self, indicators):
		self.technicalIndicators = indicators.split(' ')

	# def getLast
# ts = td.time_series(
#     symbol="EUR/USD",
#     interval="1min",
#     outputsize = 5000,
#     start_date="2020-04-10 21:18:00",
#     # end_date="2012-03-09",
#     dp = 6,
#     timezone = "Europe/Bucharest"
# ).as_pandas()
# df = ts.with_bbands(ma_type="EMA").with_plus_di().with_wma(time_period=20).with_wma(time_period=40).as_pandas()

# print(ts)
# print(df)


# 1. Returns OHLCV chart
# ts.as_pyplot_figure()
# print(ts.as_pandas())

# 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
# df = ts.with_ma(dp="10").with_rsi(dp="10").with_macd(dp="10").with_stoch().with_atr().as_json()
# print(df.with_bbands(dp="10")) #with_sar

# df.to_csv(r"df.csv", index = False)

data = ForexData("EUR/USD", "1day", ForexData.today, 5000)
data.setTechnicalIndicators("macd")
dtt = data.getDataWithIndicators()





