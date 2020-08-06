from collections import defaultdict 

class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.isEnd = False

class Trie:
	""" 
	return true if searched word is present in trie
	one . is considered as any of the characher   
	"""
	def __init__(self):
		self.root = TrieNode()

	def addWord(self,word):
		node = self.root
		for c in word:
			node = node.children[c]
		node.isEnd = True

	def search(self,word):
		node = self.root
		self.result = False
		self.dfs(node,word)
		return self.result

	def dfs(self,node,word):
		# terminating condition when word is ""
		if not word:
			if node.isEnd:
				self.result = True
			return
		
		if word[0] == '.':
			for d in node.children.values():
				self.dfs(d,word[1:])
		else:
			# character not present in dict
			node = node.children.get(word[0])
			# self.result is False here
			if not node:
				return	
			self.dfs(node,word[1:])
		
class WordDictionary:
	""" faster than above method """
	def __init__(self):
		self.root = {}

	def addWord(self,word):
		tree = self.root
		for c in word:
			if c not in tree:
				tree[c] = {}
			tree = tree[c]
		tree['End'] = True

	def search(self,word):
		self.result = False
		self.dfs(self.root,word)
		return self.result

	def dfs(self,node,word):
		if not word:
			if 'End' in node:
				self.result = True
			return
		
		if word[0] == '.':
			for d in node.values():
				if d is True:
					continue
				self.dfs(d,word[1:])
		else:
			if word[0] not in node:
				return
			else:
				node = node[word[0]]
			self.dfs(node,word[1:])

if __name__ == "__main__":
	inp = ['apple','apk']
	search = ['apple','app','ap','a..','a....']
	t = Trie()

	for word in inp:
		t.addWord(word)

	for word in search:
		print( word,' -> ',t.search(word) )
