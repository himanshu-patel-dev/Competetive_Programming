"""
We're going to make our own Contacts application! The application must 
perform two types of operations:

add name, where  is a string denoting a contact name. This must store  
as a new contact in the application.
find partial, where  is a string denoting a partial name to search the 
application for. It must count the number of contacts starting with partial and 
print the count on a new line.

Given  sequential add and find operations, perform each operation in order.

Sample Input
4
add hack
add hackerrank
find hac
find hak

Sample Output
2
0
"""
class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEnd = False
		# to store all the branches or path whiches passes through 
		# this node, this only prevent TLE instead of DFS to search 
		# all path starting from current node
		self.branch = 0

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self,word):
		node = self.root
		for char in word:
			i = ord(char) - ord('a')
			if node.children[i] is None:
				node.children[i] = TrieNode()
			node.branch += 1
			node = node.children[i]
		node.branch += 1
		node.isEnd = True

	def prefix(self,word):
		node = self.root
		for char in word:
			i = ord(char) - ord('a')
			if node.children[i] is None:
				return 0
			node = node.children[i]
		return node.branch

def contacts(queries):
	t = Trie()
	result = []
	for q in queries:
		if q[0] == 'add':
			t.insert(q[1])
		else:
			result.append( t.prefix(q[1]) )
	return result

if __name__ == '__main__':
	queries_rows = int(input())
	queries = []

	for _ in range(queries_rows):
		queries.append(input().rstrip().split())

	print( contacts(queries) )
