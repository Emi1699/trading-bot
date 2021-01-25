from twelvedata import TDClient
import toks


class ForexData():
	def __init__(self):
		self.client = TDClient(toks.AccessTokens().TDtoken())
		self.technicalIndicators = ["bbands", "rsi"]

	def getLastCandle(self, currencyPair, period, output = 1):
		ts = self.client.time_series(
		    symbol = currencyPair,
		    outputsize = output,
		    interval = period
		)

		return ts

	def getDataWithIndicators(self, currencyPair, period, output = 1):
		ts = self.getLastCandle(currencyPair, period, output)
		if "bbands" in self.technicalIndicators:
			ts = ts.with_bbands()
		if "macd" in self.technicalIndicators:
			ts = ts.with_macd()
		if "rsi" in self.technicalIndicators:
			ts = ts.with_rsi()

		return ts.as_pandas()

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

data = ForexData()
print(data.getDataWithIndicators("GME", "1min"))






