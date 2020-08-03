class TreeNode:
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

def Make_Tree_From_LevelOrder(LevelOrder):
	from collections import deque
	q = deque()

	n = len(LevelOrder)

	if n == 0 or LevelOrder[0] == 'N':
		return None
	i = 0	# iterator for LevelOrder Array
	root = TreeNode( int( LevelOrder[i] ) ) 
	q.append(root)
	i += 1

	while len(q) > 0 and i < n:
		CurrentNode = q.popleft()
		CurrentValue = LevelOrder[i]
		# for left child of current node
		if CurrentValue != 'N':
			CurrentNode.left = TreeNode( int(CurrentValue) )
			q.append( CurrentNode.left )

		i += 1
		if i == n:
			break
		CurrentValue = LevelOrder[i]
		# for right child of node
		if CurrentValue != 'N':
			CurrentNode.right = TreeNode( int(CurrentValue) )
			q.append( CurrentNode.right )

		i += 1
	return root


if __name__ == "__main__":
	"""      root
		_____ 1__________
		|			    |
	 ___2___		____3___
	 |		|		|		|
	_4_	  __5__	 ___6___ ___7___
   |   |  |    | |	   | |	   |
   |   N  N	   N N	   N N	   N
__100__
|	   |
N	   N
	"""
	# when None pointer is given
	LevelOrder = ['1','2','3','4','5','6','7','100','N','N','N','N','N','N','N','N','N']
	root = Make_Tree_From_LevelOrder( LevelOrder )
	print( root.Inorder([]) )

	# when None pointer is not given
	LevelOrder = [90, 15, 10, 7, 12, 2]
	root = Make_Tree_From_LevelOrder( LevelOrder )
	print( root.Inorder([]) )
