from scipy import stats, optimize, interpolate
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import collections as coll
import pickle

f = open(f'text/sample.txt', 'r', encoding="utf8")

def parseSentence(file):
	sentence = []
	sentenceList = []
	for char in file:
		if(ord(char) == 46):
			if(sentence != []):
				sentenceList.append((''.join(sentence) + ".").lower())
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
				wordList.append((''.join(word)).lower())
				word = []
		else:
			word.append(char)
	return wordList
	
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
	
def findAveSyllablePerWord(file):
	wordList = parseWords(file)
	totalSyllableCount = 0
	for word in wordList:
		totalSyllableCount += syllableCount(word)
	aveSyllable = (totalSyllableCount / len(wordList))
	return aveSyllable
	
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
	
def findAveWordLength(file):
	wordList = parseWords(file)
	totalWordLengths = 0
	for word in wordList:
		totalWordLengths += len(word)
	aveWordLength = (totalWordLengths / len(wordList))
	return aveWordLength
	
def countPuncuation(file):
	punc = [",", ".", "'", "!", '"', ";", "?", ":", ";"]
	count = 0
	for char in file:
		if (char in punc):
			count += 1
	return count / len(file)
	
def countFunctionalWords(file):
	functionalWords = """a between in nor some upon
    about both including nothing somebody us
    above but inside of someone used
    after by into off something via
    all can is on such we
    although cos it once than what
    am do its one that whatever
    among down latter onto the when
    an each less opposite their where
    and either like or them whether
    another enough little our these which
    any every lots outside they while
    anybody everybody many over this who
    anyone everyone me own those whoever
    anything everything more past though whom
    are few most per through whose
    around following much plenty till will
    as for must plus to with
    at from my regarding toward within
    be have near same towards without
    because he need several under worth
    before her neither she unless would
    behind him no should unlike yes
    below i nobody since until you
    beside if none so up your
    """
	functionalWords = functionalWords.split()
	wordsList = parseWords(file)
	
	count = 0
	for word in wordsList:
		if word in functionalWords:
			count += 1
			
	return count / len(wordsList)
	
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
	percent = (difficultWords / words) * 100
	if(percent > 5):
		adjusted = 3.6365
	return (0.1579 * (percent)) + (0.0496 * (words / sentences)) + adjusted

def fleschKincaidGradeLevel(file):
	return (0.39 * (len(parseWords(file))/len(parseSentence(file)))) + (11.8 * (totalSyllables(file) / len(parseWords(file)))) - 15.59
	
def fleschReadingEase(file):
	return 206.835 - (1.015 * (len(parseWords(file))/len(parseSentence(file)))) - (84.6 * (totalSyllables(file) / len(parseWords(file))))
	
	
def countComplexWords(file): #only for gunningFogIndex
	wordList = parseWords(file)
	complexWordList = []
	for word in wordList:
		if(syllableCount(word) >= 3):
			complexWordList.append(word)
	return complexWordList

def gunningFogIndex(file):
	return 0.4 * ( ( (len(parseWords(file))/len(parseSentence(file)))) + (100 * (len(countComplexWords(file)) / len(parseWords(file)))) )
	
def hapaxDisLegomenon(file):
	wordList = parseWords(file)
	for i, word in enumerate(wordList): wordList[i] = word.lower()
	nonUniqueWords = 0
	freq = {key: 0 for key in wordList} #creats a dict with every word as a key and their assigned value at 0. 
	for word in wordList:
		freq[word] += 1
	for word in freq:
		if freq[word] != 1:
			nonUniqueWords += 1
			
	totalSingleWords = len(set(wordList))
	
	return (nonUniqueWords / totalSingleWords)
	
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
	
def brunetsMeasureW(file):
	wordList = parseWords(file)
	N = len(wordList)
	V = len(set(wordList))
	W = (N**(V**-0.165))
			
	return W
	
def honoresRMeasure(file):
	wordList = parseWords(file)
	for i, word in enumerate(wordList): wordList[i] = word.lower()
	uniqueWords = 0
	freq = {key: 0 for key in wordList} #creats a dict with every word as a key and their assigned value at 0. 
	for word in wordList:
		freq[word] += 1
	for word in freq:
		if freq[word] == 1:
			uniqueWords += 1
			
	totalVocab = len(set(wordList))
	N = len(wordList)
	
	R = 100 * math.log(N / (1 - (uniqueWords/totalVocab)))
	
	return R
	
def sichelsMeasureS(file):
	wordList = parseWords(file)
	for i, word in enumerate(wordList): wordList[i] = word.lower()
	nonUniqueWords = 0
	freq = {key: 0 for key in wordList} #creats a dict with every word as a key and their assigned value at 0. 
	for word in wordList:
		freq[word] += 1
	for word in freq:
		if freq[word] != 1:
			nonUniqueWords += 1
			
	totalSingleWords = len(set(wordList))
	
	S = nonUniqueWords / float(len(set(wordList)))
	
	return S
	
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
	
	return 1 - (n / (N * (N - 1)))
	
# PCA -- :

#dividesText into chunks of 10-sentences
def divideText(file):
	sentenceList = parseSentence(file)
	
	chunk = []
	chunkList = []
	for i, word in enumerate(sentenceList):
		if i % 10 == 0 and i != 0:
			chunkList.append(chunk)
			chunk = []
		chunk.append(sentenceList[i])
		
	#in case the text's sentences are not perfectly divisable by 10
	if chunk != []:
		chunkList.append(chunk)
		chunk = []
		
	return chunkList
	
# ELBOW METHOD
def ElbowMethod(data):
    X = data  # <your_data>
    distorsions = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        distorsions.append(kmeans.inertia_)

    fig = plt.figure(figsize=(15, 5))
    plt.plot(range(1, 10), distorsions, 'bo-')
    plt.grid(True)
    plt.ylabel("Square Root Error")
    plt.xlabel("Number of Clusters")
    plt.title('Elbow curve')
    plt.savefig("ElbowCurve.png")
    plt.show()
	

def establishFeaturesVector(file):
	chunkList = divideText(file)

	vector = []
	featuresList = []
	
	for chunk in chunkList:
		#Lexical Features
		featuresList.append(findAveSyllablePerWord(file))
		featuresList.append(findAveSentLengthByWord(file))
		featuresList.append(findAveSentLengthByChar(file))
		featuresList.append(findAveWordLength(file))
		featuresList.append(countPuncuation(file))
		featuresList.append(countFunctionalWords(file))
		
		"""print(findAveSyllablePerWord(file))
		print(findAveSentLengthByWord(file))
		print(findAveSentLengthByChar(file))
		print(findAveWordLength(file))
		print(countPuncuation(file))
		print(countFunctionalWords(file))"""
		
		#Readability Features
		featuresList.append(daleChall(file))
		featuresList.append(fleschKincaidGradeLevel(file))
		featuresList.append(fleschReadingEase(file))
		featuresList.append(gunningFogIndex(file))
		
		"""print(daleChall(file))
		print(fleschKincaidGradeLevel(file))
		print(fleschReadingEase(file))
		print(gunningFogIndex(file))"""
		
		#Vocabularic Features
		featuresList.append(brunetsMeasureW(file))
		featuresList.append(hapaxLegomenon(file))
		featuresList.append(hapaxDisLegomenon(file))
		featuresList.append(honoresRMeasure(file))
		featuresList.append(shannonEntropy(file))
		featuresList.append(sichelsMeasureS(file))
		featuresList.append(simpsonsIndex(file))
		featuresList.append(yulesCharacteristicK(file))
		
		"""print(brunetsMeasureW(file))
		print(hapaxLegomenon(file))
		print(hapaxDisLegomenon(file))
		print(honoresRMeasure(file))
		print(shannonEntropy(file))
		print(sichelsMeasureS(file))
		print(simpsonsIndex(file))
		print(yulesCharacteristicK(file))"""
		
		vector.append(featuresList)
	
	return vector
	
featuresVector = establishFeaturesVector(f.read())
arr = (np.array(featuresVector))
featuresVector = StandardScaler().fit_transform(arr)

np.seterr(divide='ignore', invalid='ignore') #https://stackoverflow.com/questions/14861891/runtimewarning-invalid-value-encountered-in-divide
pca = PCA(n_components=2)
components = (pca.fit_transform(arr))


"""# Applying kmeans algorithm for finding centroids
K = 2
kmeans = KMeans(n_clusters=K)
kmeans.fit_transform(components)
print("labels: ", kmeans.labels_)
centers = kmeans.cluster_centers_


# lables are assigned by the algorithm if 2 clusters then lables would be 0 or 1
lables = kmeans.labels_
colors = ["r.", "g.", "b.", "y.", "c."]
colors = colors[:K + 1]"""

for i in range(len(components)):
	plt.plot(components[i][0], components[i][1], markersize=999)

plt.xlabel("1st Principle Component")
plt.ylabel("2nd Principle Component")
title = "Styles Clusters"
plt.title(title)
plt.savefig("Results" + ".png")
plt.show()

	