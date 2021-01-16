#read access tokens from external file

filepath = '/Users/emi_buliga/Desktop/tokens.txt'
tokens = []
with open(filepath, 'r') as f:
	for line in f:
		tokens.append(line.strip())

apiToken = tokens[0]
accToken = tokens[1]
