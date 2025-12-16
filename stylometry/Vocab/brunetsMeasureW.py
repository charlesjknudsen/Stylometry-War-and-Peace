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
	
def brunetsMeasureW(file):
	wordList = parseWords(file)
	N = len(wordList)
	V = len(set(wordList))
	W = (N**(V**-0.165))
			
	return W
	
print(brunetsMeasureW(f.read()))
	

	
	
