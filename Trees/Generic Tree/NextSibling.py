class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None
		self.sibling = None

def Point_Sibling(root):
	"""
	each node have a pointer called sibling and it is null if its
	the right most node in that level otherwise it points to next sibling
	its None initially fill it accordingly
	"""
	if root is None:
		return
	if root.left:
		root.left.sibling = root.right
	
	if root.right:
		if root.sibling:
			root.right.sibling = root.sibling.left
		else:
			root.right.sibling = None
	Point_Sibling(root.left)
	Point_Sibling(root.right)

def print_sibling(root):
	t = root
	while t:
		temp = t
		while temp is not None:
			print( temp.data , end=' -> ')
			temp = temp.sibling
		print()
		t = t.left

if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2____	____3____
	|		|	|		|
____4____	5	6		7
|		|
100		200
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
	a.left.right = Binary_Tree_Node(200)

	Point_Sibling(root)
	# for print and verifing purpose 
	print_sibling(root)	
	