class AccessTokens():
	def __init__(self):
		# print("\nAccessTokens Object created.\n")

		#read access tokens from external file
		filepath = '/Users/emi_buliga/Desktop/tokens.txt'
		self.tokens = []
		with open(filepath, 'r') as f:
			for line in f:
				self.tokens.append(line.strip())

	def apiToken(self):
		return self.tokens[0]

	def accToken(self):
		return self.tokens[1]
