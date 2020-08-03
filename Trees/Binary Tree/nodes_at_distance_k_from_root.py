class TreeNode:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def distance_k(root,k,result):
	""" 
	return nodes at distance k form root (root at dist 0) 
	in order from left to right 
	k = target depth, result = array to hold result
	"""
	if root is None:
		return

	if k == 0:
		result.append( root.data )
	else:
		distance_k(root.left,k-1,result)
		distance_k(root.right,k-1,result)
	
	return result


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	|
	100
	"""
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	a = root.left
	b = root.right
	a.left = TreeNode(4)
	a.right = TreeNode(5)
	b.left = TreeNode(6)
	b.right = TreeNode(7)
	a.left.left = TreeNode(100)

	print( distance_k(root,2,[]) )