f = open(f'text/sample.txt', 'r')

def countPuncuation(file):
	punc = [",", ".", "'", "!", '"', ";", "?", ":", ";"]
	count = 0
	for char in file:
		if (char in punc):
			count += 1
	return count / len(file)
	
print(countPuncuation(f.read()))
		