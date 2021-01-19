

class fileHandler:
	def __init__(self):
		print("\nfileHandler Object created.\n")

	def newEntry(self, file, content):
		f = open(file, 'a+')
		f.write(content)
		f.close()

fh = fileHandler()
fh.newEntry("emi.txt", "dqwerqwerqwer")