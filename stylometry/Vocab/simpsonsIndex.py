import collections as coll

f = open(f'text/sample.txt', 'r')

def parseWords(file):
	word = []
	wordList = []
	for char in file:
		if(ord(char) == 32 or ord(char) == 46 or ord(char) == 44 or ord(char) == 45):
			if(word != []):
				wordList.append(''.join(word))
				word = []
		else:
			word.append(char)
	return wordList

# 1 - (sigma(n(n-1))/N(N-1)
# N is total number of words
# n is the number of each type of word

def simpsonsIndex(file):
	wordsList = parseWords(file)
	individualWordFrequency = coll.Counter()
	individualWordFrequency.update(wordsList)
	N = len(wordsList)
	n = 0 
	for freq in individualWordFrequency.values():
		n += (freq * (freq - 1)) #sigma = series/summation
		print(n)
	
	return 1 - (n / (N * (N - 1)))
	
print(simpsonsIndex(f.read()))