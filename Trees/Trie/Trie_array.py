class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def getNode(self):
        return TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        length = len(word)
        level = self.root
        for i in range(length):
            index =  ord(word[i]) - ord('a')
            if not level.children[index]:
                level.children[index] = self.getNode()
            level = level.children[index]
        level.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        length = len(word)
        level = self.root
        for i in range(length):
            index =  ord(word[i]) - ord('a')
            if not level.children[index]:
                return False
            level = level.children[index]
        return  level and level.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
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
	T = Trie()
	T.insert('apple')
	print( T.search('apple') )
	print( T.search('app') )
	print( T.startsWith('app') )
