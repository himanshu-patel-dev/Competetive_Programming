class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def LCA(root,p,q):
	"""
	given two nodes p and q determine their lowest common ancestor 
	here all node need to be distinct in value (no repeted values)
	"""
	if root is None:
		return False
	if root.data == p or root.data == q:
		return root.data
	
	l = LCA(root.left, p, q)
	r = LCA(root.right,p, q)

	if l and r:
		return root.data
	else:
		return l if l else r

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

	print( LCA(root,4,4) )