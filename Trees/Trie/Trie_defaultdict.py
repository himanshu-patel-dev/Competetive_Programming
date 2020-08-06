from collections import defaultdict

class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self,word):
		t = self.root
		for c in word:
			t = t.children[c]
		t.isEnd = True

	def search(self,word):
		t = self.root
		for c in word:
			t = t.children.get(c)
			if t is None:
				return False
		return t.isEnd

	def startsWith(self,word):
		t = self.root
		for c in word:
			t = t.children.get(c)
			if t is None:
				return False
		return True

if __name__ == "__main__":
	inp = ['apple','apk']
	search = ['apple','app','ap','application']
	t = Trie()

	for word in inp:
		t.insert(word)

	for word in search:
		print( word,' -> ',t.search(word) )

	print('---------------------------------')

	for word in search:
		print( word,' -> ',t.startsWith(word) )
