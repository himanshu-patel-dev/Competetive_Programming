class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def zigzag(root):
	if root is None:
		return None

	LeftToRight = True
	CurrentLevel = []
	Result = []
	if root:
		CurrentLevel.append(root)

	while len(CurrentLevel) > 0:
		LevelResult = []
		NextLevel = []
		while len(CurrentLevel) > 0:
			n = CurrentLevel.pop()
			LevelResult.append( n.data )

			if LeftToRight:
				if n.left:
					NextLevel.append(n.left)
				if n.right:
					NextLevel.append(n.right)
			else:
				if n.right:
					NextLevel.append(n.right)
				if n.left:
					NextLevel.append(n.left)
		LeftToRight = not LeftToRight
		Result.extend( LevelResult )
		CurrentLevel = NextLevel
	return Result
				


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2____	____3____
	|		|	|		|
____4____	5	6		7
|		|
100		200
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
	a.left.right = Binary_Tree_Node(200)

	print( zigzag(root) )