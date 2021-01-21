import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data


# data = pd.read_csv('price data/EUR_USD_data',sep=',',header=None)
# # print(data)
# hour = data[1][0][1:]
# print(type(hour))
# print(hour)
# data = pd.DataFrame(data)

# x = [x[1:] for x in data[1]]
# y = data[0]
# # print(x)

# x = [datetime.strptime(elem, '%H:%M:%S') for elem in x]
# # print(x)
# (fig, ax) = plt.subplots(1, 1)
# plt.plot_date(x, y)

# plt.show()
# # ax.plot(x, y)
# # fig.show()

# # Convert string times into datetime python objects
# # dt_object1 = datetime.strptime(hour, "%H:%M:%S").time()
# # print("dt_object1 =", dt_object1)
# # [datetime.strptime(x[0][1:], "%H:%M:%S").time() for x in data[1]]
# # print([datetime.strptime(x[1:], "%H:%M:%S").time() for x in data[1]])

# # y = data[0]
# # x = [datetime.strptime(x[1:], "%H:%M:%S") for x in data[1]]
# # # plt.plot(x, y,'r--')
# # print(x)
# # dates = matplotlib.dates.date2num(x)
# # plt.plot_date(dates, y)

# # plt.show()