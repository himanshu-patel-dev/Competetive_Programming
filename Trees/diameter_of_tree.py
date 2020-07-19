class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def height(root):
	if root is None:
		return 0
	return max( height(root.left), height(root.right) ) + 1

def diameter(root):
	""" returns diameter of a tree """
	if root is None:
		return 0
	h1 = height(root.left)
	h2 = height(root.right)
	sub_dia =  max( diameter(root.left) , diameter(root.right) )
	return max( h1+h2+1, sub_dia )

if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2____	____3____
	|		|	|		|
	4		5	6		7
	|
	100
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
	a.left.left = Binary_Tree_Node(100)

	print( diameter(root) )