from twelvedata import TDClient
td = TDClient("fc8ac6249ad2462eb283fd992bb29575")


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

ts = td.time_series(
    symbol="EUR/USD",
    outputsize=5000,
    interval="1min",
)
# 1. Returns OHLCV chart
# ts.as_pyplot_figure()
# print(ts.as_pandas())

# 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
df = ts.with_ma(dp="10").with_rsi(dp="10").with_macd(dp="10").with_bbands(dp="10").with_stoch().with_atr().as_pandas()
print(df) #with_sar

df.to_csv(r"df.csv", index = False)