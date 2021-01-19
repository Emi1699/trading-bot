

class FileHandler:
	def __init__(self):
		print("\nfileHandler Object created.\n")

	def newEntry(self, file, content):
		f = open("price data/" + file, 'a+')
		f.write(content + "\n")
		f.close()