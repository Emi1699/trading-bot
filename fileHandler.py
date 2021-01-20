import os

class FileHandler:
	def __init__(self): pass
		# print("\nfileHandler Object created.\n")

	#creates a new entry in the specified file from the 'trades' directory
	def newEntry_liveData(self, file, content):
		f = open("price data/" + file + "_data", 'a+')
		f.write(content + "\n")
		f.close()

	#creates a new entry in the specified file from the 'open trades' directory
	#the line containts the id, number of units and price of the specified trade
	def newEntry_tradePlaced(self, file, content):
		f = open("open trades/" + file, 'a+')
		f.write(content + "\n")
		f.close()

	#create new entry in the specified file from the 'closed trades' directory
	#the line contains the id and the P/L of the trade (for now!!!)
	def newEntry_tradeClosed(self, file, content):
		f = open("closed trades/" + file, 'a+')
		f.write(content + "\n")
		f.close()

	#when closing a trade, we also want to delete it from the 'trades' directory
	#at the same time, add it to a 'closed trades' directory
	def removeEntry_trade(self, tradeID, file):
		#save file content into an array
		lines = []
		with open('open trades/' + file) as oldfile:
		    for line in oldfile:
		    	lines.append(line)

		#remove the file and create it again (empty)
		os.remove('open trades/' + file)
		f = open('open trades/' + file, 'a+')

		#write the content to file, except for the content we wish to delete
		for line in lines:
			if not str(tradeID) in line:
				f.write(line)

	#check if a file is empty
	#used in closing all trades in the User class
	def isEmpty(self, instrument):
		if os.stat('open trades/' + instrument).st_size == 0:
			return True

		return False











