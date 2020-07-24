class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def path_to_node(root,target,path):
	"""
	output path from root to target node in reverse order i.e. target to root
	just reverse the list 'path' after getting answer, pass [] in path when invoking
	"""
	if root is None:
		return False

	if root.data == target:
		path.append(root.data)
		return True

	l = path_to_node(root.left,target,path)
	r = path_to_node(root.right,target,path)
	if l or r:
		path.append(root.data)
		return True
	else:
		return False
		

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

	result = []
	path_to_node(root,100,result)
	result = result[::-1]
	print(result)