from collections import deque

class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None
def max_depth(root):
	if root is None:
		return 0
	return 1 + max( max_depth(root.left) , max_depth(root.right) )

def max_sum_level_util(root,level,level_sum):
	if root is None:
		return
	# sum of node at that level is added and recursive call to next level
	level_sum[ level ] += root.data
	if root.left:
		max_sum_level_util(root.left,level+1,level_sum)
	if root.right:
		max_sum_level_util(root.right,level+1,level_sum)

def max_sum_level(root):
	"""
	return level which have max sum of all element in that level
	format: ( max sum, level )  root at level = 0
	"""
	# get max no of level in tree
	level_sum = [0]*max_depth(root)
	level = 0	

	max_sum_level_util(root,0,level_sum)

	# get the level and max sum at that level, each index represent a level
	m = max(level_sum)
	index = level_sum.index(m)
	return (m,index)


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2____	___150___
	|		|	|		|
	4		5	6		7
	|
	10
	"""
	root = Binary_Tree_Node(1)
	root.left = Binary_Tree_Node(2)
	root.right = Binary_Tree_Node(150)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)
	a.left.left = Binary_Tree_Node(10)

	print( max_sum_level(root) )

