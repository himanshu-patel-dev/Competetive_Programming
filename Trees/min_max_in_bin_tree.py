class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def min_in_tree(root):
	if root is None:
		return float('inf')
	elif root.left is None and root.right is None:
		return root.data

	m = root.data
	l = min_in_tree(root.left)
	r = min_in_tree(root.right)
	return min(l,m,r)

def max_in_tree(root):
	if root is None:
		return float('-inf')
	elif root.left is None and root.right is None:
		return root.data

	m = root.data
	l = max_in_tree(root.left)
	r = max_in_tree(root.right)
	return max(l,m,r)

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
	
	print( min_in_tree(root) )
	print( max_in_tree(root) )