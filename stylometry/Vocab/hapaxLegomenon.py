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
	
def hapaxLegomenon(file):
	wordList = parseWords(file)
	for i, word in enumerate(wordList): wordList[i] = word.lower()
	uniqueWords = 0
	freq = {key: 0 for key in wordList} #creats a dict with every word as a key and their assigned value at 0. 
	for word in wordList:
		freq[word] += 1
	for word in freq:
		if freq[word] == 1:
			uniqueWords += 1
			
	totalSingleWords = len(set(wordList))
			
	return (uniqueWords / totalSingleWords)
	
print(hapaxLegomenon(f.read()))
	

	
	
