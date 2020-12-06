"""
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be 
set to NULL.
Initially, all next pointers are set to NULL.
Note: It is not a complete binary tree


Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space 
does not count as extra space for this problem.

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

Leetcode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""

class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

class Solution:
	def connect(self, root):
		curr_level = root
		next_level = node_Iter = Node()

		# iterating for each level in tree
		while curr_level:
			curr_level_node = curr_level
			# iterating for each node in current level
			while curr_level_node:
				if curr_level_node.left:			
					node_Iter.next = curr_level_node.left
					node_Iter = node_Iter.next

				if curr_level_node.right:
					node_Iter.next = curr_level_node.right
					node_Iter = node_Iter.next

				# do the same for all nodes in the next list of current level
				curr_level_node = curr_level_node.next		

			# when current level reach its end start with next level
			curr_level, node_Iter = next_level.next, next_level
			# break free the node_iter node and use it for next level
			node_Iter.next = None

		return root
