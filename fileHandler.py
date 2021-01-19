

class FileHandler:
	def __init__(self):
		print("\nfileHandler Object created.\n")

	def newEntryLiveData(self, file, content):
		f = open("price data/" + file, 'a+')
		f.write(content + "\n")
		f.close()

	def newEntryTradePlaced(self, file, content):
		f = open("trades/" + file, 'a+')
		f.write(content + "\n")
		f.close()