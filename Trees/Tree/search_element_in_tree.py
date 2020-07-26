class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def find(root, data):
	if root is None:
		return False
	if root.data == data:
		return True
	if root.left and find(root.left,data):
		return True
	if root.right and find(root.right,data):
		return True
	return False

if __name__ == "__main__":
	"""      root
		______1______
		|			|
	____2____	____3____
	|		|	|		|
	4		5	6		7
	"""
	root = Binary_Tree_Node(1)
	root.left = Binary_Tree_Node(2)
	root.right = Binary_Tree_Node(3)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)
	
	print( find(root, 5) )
	print( find(root, 10) )
	