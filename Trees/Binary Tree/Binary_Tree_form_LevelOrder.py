class TreeNode:
	""" Binary Tree Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None


def LevelOrder(root,result):
	""" T = O(n) S = O(n) """
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

	# level order traversal of above tree
	# lo = [10,5,18,3,7,16,20,2]
	lo = ['1','2','3','4','5','6','7','100']
	# lo = ['+', '*', '-', '5', '4', '100', '20']

	root = LevelOrder_to_BST(lo)
	print( LevelOrder(root,[]) )
