class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	"""
	return how many path are there with target sum
	path not necessarily start from root or end at leaf
	Tree is binary tree not necessarily bst
	"""
	def __init__(self):
		self.result = 0
		
		
	def pathSum(self, root: TreeNode, target: int) -> int:
		
		def preorder(root,curr_sum,target):
			if root is None:
				return
			
			curr_sum += root.val
			# if current sum reach target value then += 1
			if curr_sum == target:
				self.result += 1
			# if current sum is greater than target and curent - target 
			# is found in hash it means tasrget sum can also be achived 
			self.result += self.hash[curr_sum - target] 
			
			# include current sum in hash
			self.hash[curr_sum] += 1
			preorder(root.left,curr_sum,target)
			preorder(root.right,curr_sum,target)
			self.hash[curr_sum] -= 1
			
		from collections import defaultdict
		self.hash = defaultdict(int)
		preorder(root,0,target)
		return self.result


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2___	____3___
	|		|	|		|
	4		5	6		7
	|
	0
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
	a.left.left = TreeNode(0)

	s =Solution()
	# path1 = 1,2,4 and 6 and 1,2,4,0
	print( s.pathSum(root,6) )
