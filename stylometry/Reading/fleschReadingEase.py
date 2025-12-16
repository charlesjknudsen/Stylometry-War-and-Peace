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
	
def syllableCount(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count
	
def totalSyllables(file):
	totalSyllables = 0
	wordList = parseWords(file)
	for word in wordList:
		totalSyllables += syllableCount(word)
	return totalSyllables

def fleschReadingEase(file):
	return 206.835 - (1.015 * (len(parseWords(file))/len(parseSentence(file)))) - (84.6 * (totalSyllables(file) / len(parseWords(file))))
	
print(fleschReadingEase(f.read()))