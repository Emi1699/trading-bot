

class FileHandler:
	def __init__(self):
		print("\nfileHandler Object created.\n")

	#creates a new entry in the specified file from the 'trades' directory
	def newEntry_liveData(self, file, content):
		f = open("price data/" + file, 'a+')
		f.write(content + "\n")
		f.close()

	#creates a new entry in the specified file from the 'trades' directory
	#the line containts the id, number of units and price of the specified trade
	def newEntry_tradePlaced(self, file, content):
		f = open("trades/" + file, 'a+')
		f.write(content + "\n")
		f.close()

	#when closing a trade, we also want to delete it from the 'trades' directory
	def removeEntry_Trade(self, tradeID, file):
		with open('trades/' + file) as oldfile, open('trades/' + file, 'w') as newfile:
		    for line in oldfile:
		        if not tradeID in line:
		            newfile.write(line)