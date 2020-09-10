"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path 
represents a binary number starting with the most significant bit.  For example, 
if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, 
which is 13. Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22

	  1
	 / \	
	0	 1
   / \  / \
  0   1 0  1  

Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root, total = 0):
        if root is None:
            return 0

        # update value till current node
        total = (total<<1) + root.val

        # if its a leaf node then return the value till here
        if root.left is None and root.right is None:
            return total

        # get total received by each children
        l = self.sumRootToLeaf(root.left,total)
        r = self.sumRootToLeaf(root.right,total)

        return l+r
