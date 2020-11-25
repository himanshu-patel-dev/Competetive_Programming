# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	'''
		T(n) = O(n) as each node is visited only one time 
		Recursion will proceed till end in left child and then right child is processed
		then once recursion start returning then there no further call to same nodes
		S = O(1)
	'''
	def rob(self, root: TreeNode) -> int:
		def helper(node):
			if not node:
				return (0,0)
			
			left = helper(node.left)        # score obtained after robbing left sub tree
			right = helper(node.right)      # score obtained after robbing right sub tree
			
			# if we rob root then we need to return score or not robbed children
			rob = node.val + left[1] + right[1]
			
			# else we return score obtained from robbed child node
			not_rob = max(left) + max(right)
			
			# return ans of both cases robbed and not robbed
			return [rob, not_rob]
		
		return max(helper(root))



