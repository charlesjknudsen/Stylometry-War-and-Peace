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
	
def findAveWordLength(file):
	wordList = parseWords(file)
	totalWordLengths = 0
	for word in wordList:
		totalWordLengths += len(word)
	aveWordLength = (totalWordLengths / len(wordList))
	return aveWordLength
	
print(findAveWordLength(f.read()))
		

