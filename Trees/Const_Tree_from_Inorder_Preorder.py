class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def PreOrder(root,result):
	""" recursive T = O(n) S = O(n) """
	if root is None:
		return
	result.append( root.data )
	PreOrder(root.left, result)
	PreOrder(root.right, result)
	return result

def Inorder(root,result):
	""" recursive T = O(n) S = O(n)"""
	if root is None:
		return
	Inorder(root.left,result)
	result.append(root.data)
	Inorder(root.right,result)
	return result

def construct_tree(root, preorder, inorder):
	if not inorder:
		return None
	data = preorder[0]
	index = inorder.index(data)
	root = Binary_Tree_Node(data)
	root.left = construct_tree( root.left, preorder[1:index+1], inorder[:index] )
	root.right = construct_tree( root.right, preorder[index+1:], inorder[index+1:] )
	return root

if __name__ == "__main__":
	pre 	= [1, 2, 4, 100, 5, 3, 6, 7]
	inodr 	= [100, 4, 2, 5, 1, 6, 3, 7]

	r = construct_tree(None, pre, inodr )
	print( PreOrder(r,[]) )
	print( Inorder(r,[]) )

"""     	 root
		_____ 1______
		|			|
	____2____	____3____
	|		|	|		|
	4		5	6		7
	|
	100
"""