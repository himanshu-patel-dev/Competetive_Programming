class TreeNode:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def sub_max_nodes_level(root,level,result):
	if root is None:
		return
	
	result[level] += 1
	sub_max_nodes_level(root.left,level+1,result)
	sub_max_nodes_level(root.right,level+1,result)
	return result
	

def max_nodes_level(root):
	from collections import defaultdict
	# this dict contains the count of nodes for each level
	result = defaultdict(int)

	sub_max_nodes_level(root,0,result)

	level, count = 0, 0
	for ele, c in result.items():
		# choose the level with max nodes
		if c > count:
			level = ele
			count = c 
		# if number of nodes are same for two level 
		# then choose least level (closer to root)
		elif c == count and ele < level:
			level = ele
	return (level,count)


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	|
	100
	"""
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	a = root.left
	b = root.right
	a.left = TreeNode(4)
	a.right = TreeNode(5)
	b.left = TreeNode(6)
	b.right = TreeNode(7)
	a.left.left = TreeNode(100)

	# level 2 with 4 nodes
	print( max_nodes_level(root) )