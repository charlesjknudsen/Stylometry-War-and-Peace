import pickle

f = open(f'text/sample.txt', 'r')

def parseWords(file):
	word = []
	wordList = []
	for char in file:
		if(ord(char) == 32 or ord(char) == 46 or ord(char) == 44 or ord(char) == 45):
			if(word != []):
				wordList.append((''.join(word)).lower())
				word = []
		else:
			word.append(char)
	return wordList
	
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
	

def daleChall(file):
	wordList = parseWords(file)
	sentenceList = parseSentence(file)
	difficultWords = 0
	familiarWords = 0
	adjusted = 0
	words = len(wordList)
	sentences = len(sentenceList)
	with open('daleChall.pkl', 'rb') as f:
		familiarWords = pickle.load(f)
	for word in wordList:
		if word not in familiarWords:
			difficultWords += 1
	print(difficultWords)
	percent = (difficultWords / words) * 100
	if(percent > 5):
		adjusted = 3.6365
	return (0.1579 * (percent)) + (0.0496 * (words / sentences)) + adjusted
	
print(daleChall(f.read()))
