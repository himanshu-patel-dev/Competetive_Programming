from collections import deque

class Binary_Tree_Node:
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

def deepestNode(root):
	if root is None:
		return None
	q = deque()
	q.append(root)
	while len(q) > 0:
		n = q.popleft()
		if n.left:
			q.append(n.left)
		if n.right:
			q.append(n.right)
	return n

def delete_node(root,data):
	if root is None:
		return None

	q = deque()
	q.append(root)
	while len(q) > 0:
		toDelete = q.popleft()
		if toDelete.data == data:
			break
		if toDelete.left:
			q.append(toDelete.left)
		if toDelete.right:
			q.append(toDelete.right) 
	# replacing data in node we want to delete by the deepest node
	replaceBy = deepestNode(root)
	toDelete.data = replaceBy.data

	# to delete last node
	# q = deque()
	q.clear()
	q.append(root)
	while len(q) > 0:
		n = q.popleft()
		if n.left is replaceBy:
			n.left = None
			break
		else:
			q.append(n.left)
		if n.right is replaceBy:
			n. right = None
			break
		else:
			q.append(n.right)

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

	print( LevelOrder(root,[]) )
	delete_node(root,3)
	print( LevelOrder(root,[]) )