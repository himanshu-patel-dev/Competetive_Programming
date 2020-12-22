'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node 
differ in height by no more than 1.
'''

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
		self.res = True
		self.height(root)
		return self.res
		
	def height(self,root):
		if not root:
			return 0
		
		left = self.height(root.left)
		right = self.height(root.right)
		
		if abs(left-right) > 1:
			self.res = False
			
		return max(left,right)+1
