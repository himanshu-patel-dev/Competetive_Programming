'''
Given the root of a binary tree, the depth of each node is 
the shortest distance to the root. Return the smallest subtree
such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible 
among any node in the entire tree. The subtree of a node is tree 
consisting of that node, plus the set of all descendants of that node.

Leetcode: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
'''

'''
Solution:

T = O(N)
S = O(N)
'''

# Definition for a binary tree node.

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	 # The result of a subtree is:
	# Result[0]: the largest depth node that is equal to or
	#              an ancestor of all the deepest nodes of this subtree.
	# Result[1]: the number of nodes in the path from the root
	#              of this subtree, to the deepest node in this subtree.
	def subtreeWithAllDeepest(self, root):
		def dfs(node):
			if not node:
				return (None,0)

			# this rec step rec reach till leafs and then start returning
			left, right = dfs(node.left), dfs(node.right)

			# if deepness of left is more then answer lies in left side
			# return left node as current node and right node are no longer an
			# option
			if left[1] > right[1]:
				return (left[0],left[1]+1)
			# deepness of right side is more than return the right node as 
			# current node and left node are not an option
			if right[1] > left[1]:
				return (right[0],right[1]+1)

			# if deepness of both node is same then return current node 
			return (node,left[1]+1)

		return dfs(root)[0]

if __name__ == "__main__":
	# pass an example [3,5,1,6,2,0,8,null,null,7,4]
	root = TreeNode(3)
	root.left = TreeNode(5)
	root.right = TreeNode(1)

	l = root.left
	r = root.right

	r.right = TreeNode(8)
	r.left = TreeNode(0)
	l.right = TreeNode(2)
	l.left = TreeNode(6)
	l.right.right = TreeNode(4)
	l.right.left = TreeNode(7)

	s = Solution()
	res = s.subtreeWithAllDeepest(root)
	# get result as node (2) i.e. sub tree [2,7,4]
	print( res.val )


