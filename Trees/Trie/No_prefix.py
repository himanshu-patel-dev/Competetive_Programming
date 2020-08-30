"""
The set of N strings is said to be GOOD SET if no string is prefix of another 
string else, it is BAD SET. If two strings are identical, they are considered 
prefixes of each other.

Sample Input00
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

Sample Output00
BAD SET
aabcde

Sample Input01
4
aab
aac
aacghgh
aabghgh

Sample Output01
BAD SET
aacghgh
"""
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            i = ord(char) - ord('a')
            # if node is already end node of some word
            if node.isEnd:
                return False
            # add child to current node if not present 
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        
        # if last node is also end node then 
        # there are two same words
        if node.isEnd:
            return False
        node.isEnd = True
        
        # if last node have childeren it means current 
        # word is prefix to some words
        for child in node.children:
            if child:
                return False
        return True

def NoPrefix(words):
    t = Trie()
    for w in words:
        flag = t.insert(w)
        if not flag:
            print("BAD SET")
            print(w)
            return
    print('GOOD SET')

if __name__ == '__main__':
    n = int(input())
    words = []

    for _ in range(n):
        words.append(input().rstrip())
    
    NoPrefix(words)
