class TreeNode:
	""" Binary Tree Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def LevelOrder_to_BST(lo):
	""" convert a level order traversal to a tree may not be BST """
	n = len(lo)
	root = TreeNode(lo[0])
	from collections import deque
	q = deque()
	q.append(root)
	i = 1

	while len(q) > 0 and i < n:
		node = q.popleft()
		
		# getting the left child
		node.left = TreeNode(lo[i])
		q.append( node.left )
		
		i += 1
		if i == n:
			return root

		# getting right child
		node.right = TreeNode(lo[i]) 
		q.append( node.right )
		i += 1
		
	return root

def Eval_Expression(root):
	if root is None:
		return 0
	
	if root.left is None and root.right is None:
		return int( root.data )

	l = Eval_Expression(root.left)
	r = Eval_Expression(root.right)

	if root.data == '+':
		result = l+r
	elif root.data == '-':
		result = l-r
	elif root.data == '*':
		result = l*r
	else:
		# not floored divison because -10//6 = -2 
		# while we want int(-10/6) = int(-1.6666) = -1
		result = l/r
	return int(result)

if __name__ == "__main__":
	"""
			root
			 +
		   /   \
		  *     -
		/  \   / \
		5   4 100 20

		exp = (5*4) + (100-20) = 100
	"""

	# given is the level order of expression tree
	lo = ['+', '*', '-', '5', '4', '100', '20']
	# from given level order form expression tree
	root = LevelOrder_to_BST(lo)
	# now evaluate expression tree
	print( Eval_Expression(root) )