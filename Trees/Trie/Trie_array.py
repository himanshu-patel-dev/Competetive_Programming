class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def getNode(self):
        return TrieNode()
        
    def insert(self, word: str) -> None:
        length = len(word)
        level = self.root
        for i in range(length):
            index =  ord(word[i]) - ord('a')
            if not level.children[index]:
                level.children[index] = self.getNode()
            level = level.children[index]
        level.isEnd = True

    def search(self, word: str) -> bool:
        length = len(word)
        level = self.root
        for i in range(length):
            index =  ord(word[i]) - ord('a')
            if not level.children[index]:
                return False
            level = level.children[index]
        return  level and level.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        level = self.root
        for i in range(length):
            index =  ord(prefix[i]) - ord('a')
            if not level.children[index]:
                return False
            level = level.children[index]
        if level is None:
            return False
        else:
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
