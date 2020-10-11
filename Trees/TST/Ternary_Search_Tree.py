class TSTNode:
	def __init__(self,x) -> None:
		self.char = x
		self.right = None
		self.left = None
		self.middle = None
		self.isleaf = False

class TST:
	def __init__(self) -> None:
		self.root = None
	
	def put(self,word):
		""" put a word in TST of root """
		# update the root after insertion of word
		self.root = self.putItem(self.root,word,0)

	def putItem(self,node,word,index):
		""" put a word in subtree of node """
		# get current char of word we want to insert
		c = word[index]

		# if node is none then create a node with current char and cont
		if not node:
			node = TSTNode(c)

		if c < node.char:
			node.left = self.putItem(node.left,word,index)
		elif c > node.char:
			node.right = self.putItem(node.right,word,index)
		elif index < len(word)-1:	# if this is not the last char of word
			node.middle = self.putItem(node.middle,word,index+1)
		else:
			node.isleaf = True
		
		return node

	def get(self,word):
		""" return True if node is found else False """
		node = self.getItem(self.root,word,0)

		if not node:
			return False
		return True

	def getItem(self,node,word,index):
		# get current char of word we want to insert
		c = word[index]

		# if node is none then create a node with current char and cont
		if not node:
			return None

		if c < node.char:
			return self.getItem(node.left,word,index)
		elif c > node.char:
			return self.getItem(node.right,word,index)
		elif index < len(word)-1:	# if this is not the last char of word
			return self.getItem(node.middle,word,index+1)
		else:
			return node
		
	def ExploreTST(self):
		""" return a list of all words in tree in sorted order """
		words = []
		self.ExploreSub(self.root,words,"")
		return words

	def ExploreSub(self,node,words,string):
		# similar to inorder traversal of BST

		if not node:
			return

		# traverse left sub tree
		self.ExploreSub(node.left,words,string)

		# prcess current node
		if node.isleaf:
			words.append(string+node.char)

		# traverse middle sub tree
		self.ExploreSub(node.middle,words,string+node.char)

		# traverse right sub tree
		self.ExploreSub(node.right,words,string)

if __name__ == "__main__":
	tst = TST()

	tst.put("Apple")
	tst.put("Mango")

	print(tst.get("Mango"))
	print(tst.get("Carrot"))

	tst.put("Carrot")
	print(tst.get("Carrot"))

	data = tst.ExploreTST()
	print(data)