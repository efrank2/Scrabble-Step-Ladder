"""
Quora Challenge: Scrabble Ladder
Eric Frank
September 23rd 2013 12:17 PM

Solution: Begin by isolating words of specified length. Build a graph in which adjacent words
are edit distance one apart. Two types of edges are defined, those that start at the greater
word value and those that end there. To generate a scrabble ladder start at any node and extend
both ways.

"""

points = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

#Defining a vertex object prevents the program from having to recalculate the scrabble value each time.
class vertex:
	maxPath = -1
	def __init__(self, word):
		self.word = word
		self.val = 0
		for letter in word:
			self.val += points[letter]
	def getVal(self):
		return val
	def getWord(self):
		return word
	def setMaxPath(max):
		maxPath = max

class edge:
	def __init__(self, source, sink):
		self.source = source
		self.sink = sink
	def getSource:
		return source
	def getSink:
		return sink
		
class graph:
#Declare an empty dictionary.
	def __init__(self):
		nodes = dict()
#Add a new vertex to the dictionary. The list will contain adjacent vertices.
	def addNode(vertex):
		nodes[vertex] = []
#Pop the existing list of adjacent vertices (or empty list if no adjacent words have been declared) and append new adj vertex.
	def addEdge(vertex1, vertex2):
		nodes[vertex1] = nodes.pop(vertex1).append(vertex2)

#Depth First Search
	def longestPath(vertex1):
		path = []
		stack = [vertex1]
		while stack != []:
			v = stack.pop()
			if v not in path:
				path.append(v)
			for w in reversed(nodes[v]):
				if w not in path:
					stack.append(w)
		return path

def score(word):
	return sum([points[i] for i in word])

def readIn():
#Split raw input by new line chars.
	wordlist = raw_input().split('\n')
#Filters the list and only keeps words of length K, which is found on the first input line.
	wordlist = filter(lambda w: len(w) == worldlist[0], wordlist)
#Generate a graph and populate it with word nodes.
	g = graph()
	for s in wordlist:
		v = vertex(s,score(s))
		g.addNode(v)
		
#Checks if the edit distance between the two input words is one. Returns true if so, false otherwise.
#It is assumed that both words are the same length because a filter for that has already been applied.
def editDist(word1, word2):
	diff = 0
	for ch1, ch2 in zip(word1, word2):
		if ch1 != ch2:
			diffs += 1
	if diffs == 1:
		return True
	else:
		return False

