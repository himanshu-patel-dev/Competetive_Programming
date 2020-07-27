class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None		# points to forward node
		self.left = None		# points to backward node

# another way to use static or global variable is to create 
# a instance of this class and access the var through it
class ST:	# static variable class
	def __init__(self):
		self.prev = None
		self.head = None

def print_list(head):
	while head.right:
		print(head.data,end=' -> ')
		head = head.right
	print(head.data)

def BST_to_DLL(root,prev,head):
	""" BST to Double linked list """
	if root is None:
		return
	# BST_to_DLL(root.left,st)
	BST_to_DLL(root.left,prev,head)

	if prev[0] is None:
		head[0] = root
	else:
		root.left = prev[0]
		prev[0].right = root
	# updating prev node to point to current node
	prev[0] = root

	BST_to_DLL(root.right,prev,head)

if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = BST_Tree_Node(10)
	root.left = BST_Tree_Node(5)
	root.right = BST_Tree_Node(18)
	a = root.left
	b = root.right
	a.left = BST_Tree_Node(3)
	a.right = BST_Tree_Node(7)
	b.left = BST_Tree_Node(16)
	b.right = BST_Tree_Node(20)
	a.left.left = BST_Tree_Node(2)

	head = [None]
	prev = [None]
	BST_to_DLL(root,prev,head)
	print_list(head[0])