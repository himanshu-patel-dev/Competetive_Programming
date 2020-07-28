class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def sort_BST(root,inorder=[]):
	""" inorder traversal of BST is sorted bst data """
	if root is None:
		return
	sort_BST(root.left, inorder)
	inorder.append(root.data)
	sort_BST(root.right, inorder)
	return inorder

def array_to_BST(array,n):
	""" take sorted array and its len and return root of BST """
	if n == 0:
		return None
	if n == 1:
		return BST_Tree_Node(array[0])
	
	mid = n//2
	root = BST_Tree_Node(array[mid])
	root.left = array_to_BST(array[:mid],mid)
	root.right = array_to_BST(array[mid+1:],n-mid-1)
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
	array = [2,3,5,7,10,16,18,20]
	# array = [3,10,30]
	root = array_to_BST(array,len(array))
	print( root.data )
	print( sort_BST(root) )

