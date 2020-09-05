class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def delete_node(root,data):
	if root is None:
		return None
 
	if root.data == data:
		# if both child are present
		if root.left and root.right:
			
			# get the min in right sub tree
			temp = root.right
			while temp.left:
				temp = temp.left

			# delete current node
			root.data = temp.data
			# here temp do not have left child only two case possible no 
			# child or right child may be present thus it take O(1) for 
			# algo to delete temp in rst and not infinite rucresion is 
			# possible
			root.right = delete_node(root.right,temp.data)
	
		# if only left child present return it
		elif root.left:
			return root.left

		# if only right child is present return it
		else: 
			return root.right

	# if root is more than target then go left and update the left child
	elif root.data > data:
		root.left = delete_node(root.left,data)		
	
	# if root is less than target then go right and update the right child
	else:	# root.data < data
		root.right = delete_node(root.right,data)
	
	return root


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

	from sort_BST import sort_BST
	root = delete_node(root,18)
	print( sort_BST(root,[]) )

	root = delete_node(root,5)
	print( sort_BST(root,[]) )
