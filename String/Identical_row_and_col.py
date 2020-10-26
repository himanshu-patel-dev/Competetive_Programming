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

def row_col_equal(matrix):
	"""
	Verify whether there is any pair of row and col which are identical
	Note: Here I am using TST, a trie can also be used and instead of col we can
	put row in tree 
	"""

	row,col = len(matrix), len(matrix[0])
	if row != col:
		return False

	tst = TST()

	# put all row in TST
	for r in matrix:
		tst.put(r)

	# iterate over each col 
	# now if col match with any of the row in matrix we get a match
	# in single pass of TST only because in one pass a col is verified against 
	# all rows 

	matrix_T = [ [ matrix[r][c] for r in range(row)] for c in range(col) ]

	# check for match of col with rows
	for c in matrix_T:
		if tst.get(c):
			return True
	return False


if __name__ == "__main__":
	
	# first col is same as first row
	matrix = [
		[1,2,3],
		[2,3,4],
		[3,4,5]
	]

	print( row_col_equal(matrix) )
	

	# no col is same as any row
	matrix = [
		[1,2,3],
		[2,3,4],
		[5,6,5]
	]

	print( row_col_equal(matrix) )
