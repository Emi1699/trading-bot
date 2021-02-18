from user import User
import threading
import time

user = User()
# print(user.getOpenPositions("EUR_USD"))
# user.placeTrade(235, "EUR_USD")

# user.closeAllTrades("EUR_USD")

def getdata():
	user.streamLiveQuotes("EUR_USD")

def tradee():
	while True:
		user.placeTrade(100, "EUR_USD")
		print("\nwaiting 5...\n")
		time.sleep(5)

# getdata()

t1 = threading.Thread(target = getdata)
t2 = threading.Thread(target = tradee)

t1.start()
t2.start()
