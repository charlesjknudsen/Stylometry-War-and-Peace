import collections as coll
import math
f = open(f'text/sample.txt', 'r')

def parseWords(file):
	word = []
	wordList = []
	for char in file:
		if(ord(char) == 32 or ord(char) == 46 or ord(char) == 44):
			if(word != []):
				wordList.append(''.join(word))
				word = []
		else:
			word.append(char)
	return wordList
	
def yulesCharacteristicK(file):
	wordList = parseWords(file)
	N = len(wordList)
	freqs = coll.Counter()
	freqs.update(wordList)
	vi = coll.Counter()
	vi.update(freqs.values())
	M = sum([(value * value) * vi[value] for key, value in freqs.items()])
	K = 10000 * (M - N) / math.pow(N, 2)
	
	return K
	
print(yulesCharacteristicK(f.read()))