from collections import deque

class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def leaf_and_full_nodes(root):
	""" return number of leaf (no children) and full (two children) nodes """
	if root is None:
		return 0
	leafNode = fullNode = 0
	q = deque()
	q.append(root)
	while len(q) > 0:
		n = q.popleft()
		if n.left is None and n.right is None:
			leafNode += 1
		if n.left and n.right:
			fullNode += 1
		if n.left:
			q.append(n.left)
		if n.right:
			q.append(n.right) 
	return (leafNode, fullNode)

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

	print( leaf_and_full_nodes(root) )