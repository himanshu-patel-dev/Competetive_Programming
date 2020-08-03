class Binary_Tree_Node:
	def __init__(self,data):
		""" initialize initial root node """
		self.data = data
		self.right = None
		self.left = None

	def Inorder(self,result=[]):
		""" pass an empty list each time """
		if self is None:
			return
		# calculate left child
		if self.left:
			self.left.Inorder(result)
		
		# calculate root
		result.append(self.data)
		
		# calculate right child
		if self.right:
			self.right.Inorder(result)
		return result


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

	print( root.Inorder([]) )
	print( a.Inorder([]) )