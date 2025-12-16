from scipy import stats, optimize, interpolate
import numpy as np
import collections as coll

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

def shannonEntropy(file):
	wordList = parseWords(file)
	length = len(wordList)
	freqs = coll.Counter()
	freqs.update(wordList)
	arr = np.array(list(freqs.values()))
	distribution = 1. * arr
	distribution /= max(1, length)
	sE = stats.entropy(distribution, base=2)
	return sE
	
print(shannonEntropy(f.read()))
