"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried 
(in order from oldest to newest, including this letter just queried) spell one of the words 
in the given list.

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
"""

class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self,word):
		n = len(word)
		current = self.root

		for i in range(n):
			index = ord(word[i]) - ord('a')
			if current.children[ index ] is None:
				current.children[ index ] = TrieNode()
			current = current.children[ index ]
		current.isEnd = True

class StreamChecker:
	def __init__(self, words):
		# keep track of letters received in query
		self.letters = []
		# trie to strore words in reversed order
		self.trie = Trie()
		for w in words:	
			self.trie.insert(w[::-1])

	def query(self, letter: str) -> bool:
		# append the current char ord value to letters array
		self.letters.append( ord(letter) - ord('a') )
		# get the trie
		node = self.trie.root
		# get the last index of letters and move to index 0
		# i.e. last k letter if present in trie then return True
		index = len(self.letters)-1

		while index >= 0:
			# if current prefix traversed is present in tree than return true
			if node.isEnd:
				return True
			# if current char is not in prefix of tree then check for other letters
			# for current letter check whether there exist a child in current node
			node = node.children[ self.letters[index] ] 
			if node is None:	# if node is non it means no prefix present
				return False
			index -= 1
		return node.isEnd
