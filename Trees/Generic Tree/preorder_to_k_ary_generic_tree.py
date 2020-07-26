import math

class GenericTreeNode:
	def __init__(self,data=None):
		self.data = data
		self.childList = []

def k_ary_tree(preorder,n,k,h,index):
	if n == 0:
		return None
	i = index[0]
	node = GenericTreeNode(preorder[i])
	index[0] += 1

	if index[0] < n and h > 1:
		for child in range(k):
		 	node.childList.append( k_ary_tree(preorder,n,k,h-1,index) )
	return node

def preorder_to_K_ary_Tree(preorder,k):
	n = len(preorder) 
	# height here is 1 index, i.e. height of single node = 1
	height = math.log( (k-1)*n + 1, k )
	index = [0]
	return k_ary_tree(preorder,n,k,height,index)

def postorder(root,post):
	if root is None:
		return None
	for child in root.childList:
		postorder(child,post)
	post.append(root.data)

if __name__ == "__main__":
	"""
	  _______1_____
	__2__  __3__  4
	| | |  | | |
	5 6 7  8 9 10
	"""
	preorder = [1, 2, 5, 6, 7, 3, 8, 9, 10, 4]

	root = preorder_to_K_ary_Tree(preorder,3)

	post = []
	postorder(root,post)
	# [5, 6, 7, 2, 8, 9, 10, 3, 4, 1]
	print( post )
