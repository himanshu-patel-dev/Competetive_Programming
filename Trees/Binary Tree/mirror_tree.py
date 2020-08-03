class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def LevelOrder(root,result):
	if root is None:
		return

	from collections import deque
	q = deque()
	q.append(root)

	while len(q) != 0:
		node = q.popleft()
		result.append(node.data)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	return result

def mirror_tree(root):
	""" mirror the binary tree i.e. make left child right and right child left """
	if root is None:
		return None
	# object get passed by reference ( same obj diff reference  ) 
	# thus whatever changes are done to root.left and root.right are actually 
	# done to root also
	mirror_tree(root.left)
	mirror_tree(root.right)

	# now as the children are already mirrored we just need to swap left and right
	root.left, root.right = root.right, root.left
	# no need to return anything as changes are done to argument passed 

def are_mirror(root1,root2):
	if root1 is None and root2 is None:
		return True
	# if only one of the node is none then its a mismatch
	if root1 is None or root2 is None:
		return False
	l = are_mirror(root1.left, root2.right)
	r = are_mirror(root1.right, root2.left)
	return l and r

if __name__ == "__main__":
	"""
				root	
			_____ 1______
			|			|
		____2___	____3___
		|		|	|		|
	____4____	5	-6		-7
	|		|
	11		12

			 root	
		_____ 1______
		|			|
	____3___	____2___
	|		|	|		|
	-7		-6	5	____4____
					|		|
					12		11
	"""
	root = Binary_Tree_Node(1)
	root.left = Binary_Tree_Node(2)
	root.right = Binary_Tree_Node(3)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(-6)
	b.right = Binary_Tree_Node(-7)
	a.left.left = Binary_Tree_Node(11)
	a.left.right = Binary_Tree_Node(12)

	import copy
	root1 = copy.deepcopy(root)		# deep copy
	root2 = copy.copy(root)			# shallow copy
	print( "ID root2 and root2: ",id(root1), id(root2) )
	print( 'Before Mirror: ',LevelOrder(root1, []) )
	# roo1 got mirrored, root2 is same as previous
	mirror_tree(root1)
	print( "After Mirror: ", LevelOrder(root1, []) )

	print( "Are Mirrors: ", are_mirror(root1, root2) )

