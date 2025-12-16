# I stole this from a stackoverflow post. Thanks Jeremy McGibbon, you're a lifesaver, man.
# https://stackoverflow.com/questions/46759492/syllable-count-in-python

f = open(f'text/sample.txt', 'r')

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
	
def findAveSyllablePerWord(file):
	wordList = parseWords(file)
	print(len(wordList))
	totalSyllableCount = 0
	for word in wordList:
		totalSyllableCount += syllableCount(word)
	aveSyllable = (totalSyllableCount / len(wordList))
	return aveSyllable
	
print(findAveSyllablePerWord(f.read()))