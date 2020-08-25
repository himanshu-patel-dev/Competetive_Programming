class TrieNode:
	def __init__(self):
		children = [None]*26
		isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def get_node(self):
		return TrieNode()

	def insert(self,word):
		n = len(word)
		current = self.root

		for i in range(n):
			index = ord(word[i]) - ord('a')
			if current.children[ index ] is None:
				current.children[ index ] = self.get_node()
			current = current.children[ index ]
		current.isEnd = True

class StreamChecker:
	def __init__(self, words):
		# keep track of letters received in query
		self.letters = []
		# trie to strore words in reversed order
		self.root = Trie()
		for w in words:	
			self.root.insert(w[::-1])

	def query(self, letter: str) -> bool:
		# append the current char ord value to letters array
		self.letters.append( ord(letter) - ord('a') )
		# get the trie
		node = self.root
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
				return None
		return False