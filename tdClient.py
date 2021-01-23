from twelvedata import TDClient
td = TDClient("fc8ac6249ad2462eb283fd992bb29575")


ts = td.time_series(
    symbol="EUR/USD",
    interval="1min",
    outputsize = 1,
    # start_date="2021-01-08",
    # end_date="2012-03-09",
    dp = 6,
    timezone = "Europe/Bucharest"
).as_pandas()

print(ts)