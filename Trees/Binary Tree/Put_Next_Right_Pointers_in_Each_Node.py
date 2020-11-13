'''
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

# Definition for a Node.
class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL. Initially, all next pointers 
are set to NULL.

Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

'''

class Solution:
	'''
		T = O(n)
		S = O(1)
	'''
	def connect(self, root):
		# it is a complete binary tree if root or left is none then it 
		# dont have a right child either thus return 
		if not root or not root.left:
			return root
		
		# get the left and right child of current node (right may be None but not left) 
		left, right = root.left, root.right
		# let the left child point to right child as Next
		left.next = right
		

		# go through all right child of left sub tree 
		# and let them refer left child of right sub tree
		while left.left:
			left, right = left.right, right.left
			left.next = right
		
		# repeat the process for left and right sub tree
		root.left = self.connect(root.left)
		root.right = self.connect(root.right)
		return root

'''
	T = O(n)
	S = O(1)
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # iterator for all levels
        currLevel = root
        
        # until left child is not none iterate each level 
        # at last level of complete-tree left become none
        while currLevel.left:
            
            # save pointer to next level, we need this while we 
            # finish up iterating current level and start iterating 
            # next level in same way
            nextLevel = currLevel.left
            
            # for each node of curr level populate next pointer of next level
            while currLevel:
                # link the sibling of same parent
                currLevel.left.next = currLevel.right
        
                # also link the sibling of different parent
                # if next pointer is not None then then make its child 
                # as next of current child
                if currLevel.next is not None:
                    # its a complete tree so right child cant exist without left child
                    # just create a link in bw left and right of adj nodes
                    currLevel.right.next = currLevel.next.left
        
                # moving to adj node of curr node
                currLevel = currLevel.next
        
        
            # start for next level from left child as first child 
            # of linear list of Next pointers
            currLevel = nextLevel
        
        return root
