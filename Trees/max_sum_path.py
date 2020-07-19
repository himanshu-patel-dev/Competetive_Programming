class Binary_Tree_Node:
	"""
	class for making a binary tree
	"""
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

def max_path_sum_root_to_leaf(root):
	"""
	return max sum possible from root to any of the leaf
	"""
	if root is None:
		return 0
	# return which ever child give max value plus node data itself
	return root.data + max( max_path_sum_root_to_leaf(root.left), 
							max_path_sum_root_to_leaf(root.right) )

def max_path_sum_AnyNode_util(root,s):
	if root is None:
		return 0
	# get max from both child
	l = max_path_sum_AnyNode_util(root.left,s)
	r = max_path_sum_AnyNode_util(root.right,s)
	# choose max among root node and child value, here we basically 
	# decide whether data coming from child node can help get us better (if +ve value)
	# or root data itself is sufficient (if child give 0 or -ve value)
	one_side = max(root.data, max(l,r) + root.data)
	# here we decide whether we can get better value by merging path from 
	# both left or right side, i.e. ancestor of root not included in path
	both_side = max(l+r+root.data, one_side)

	s[0] = max( s[0], both_side )
	return one_side

def max_path_sum_AnyNode(root):
	"""
	return max sum possible from one node to any other node
	"""
	# here we need to use pass by reference so that result can be updated
	# as on every update, this is the practival way to use pass by ref in python
	s = [ float('-inf') ]
	max_path_sum_AnyNode_util(root,s)
	return s[0]

def given_sum_path(root,target, till_now):
	""" 
	return true if target sum found in path else false
	path must be from root to any of the node not necessarily leaf
	till_now refers to sum we have till now at the current node from root
	"""
	if root is None:
		return False
	if target == till_now:
		return True
	if root.left is None and root.right is None:
		return target == (till_now + root.data)

	l = given_sum_path(root.left, target, root.data + till_now)
	r = given_sum_path(root.right, target, root.data + till_now)
	return l or r

if __name__ == "__main__":
	"""      root	
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	-6		-7
	|
	11
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

	print( max_path_sum_root_to_leaf(root) )
	print( max_path_sum_AnyNode(root) )
	print( given_sum_path(root, -2, 0) )
