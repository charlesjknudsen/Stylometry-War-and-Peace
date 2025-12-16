f = open(f'text/sample.txt', 'r')

def parseSentence(file):
	sentence = []
	sentenceList = []
	for char in file:
		if(ord(char) == 46):
			if(sentence != []):
				sentenceList.append(''.join(sentence) + ".")
				sentence = []
		else:
			sentence.append(char)
	return sentenceList
	
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
	
def findAveSentLengthByWord(file):
	sentenceList = parseSentence(file)
	wordList = parseWords(file)
	aveSentLength = (len(wordList) / len(sentenceList))
	return aveSentLength
	
def findAveSentLengthByChar(file):
	sentenceList = parseSentence(file)
	wordList = parseWords(file)
	totalWordLengths = 0
	for word in wordList:
		totalWordLengths += len(word)
	aveWordLength = (totalWordLengths / len(sentenceList))
	return aveWordLength
	
print(findAveSentLengthByWord(f.read()))
		

