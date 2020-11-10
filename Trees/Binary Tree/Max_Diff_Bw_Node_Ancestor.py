'''
Given the root of a binary tree, find the maximum value V for which there exist 
different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any 
child of A is an ancestor of B.

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Input: root = [1,null,2,null,0,3]
Output: 3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxAncestorDiff(self, root):
		''' T = O(n) S= O(1) '''
		def Min_Max_Child(root,mi,mx):
			if not root:
				return 

			self.res = max( self.res, abs(root.val-mi), abs(root.val-mx) )

			mi = min(mi, root.val)
			mx = max(mx, root.val)
			Min_Max_Child(root.left,mi,mx)
			Min_Max_Child(root.right,mi,mx)

		self.res = 0
		Min_Max_Child(root,root.val,root.val)
		return self.res