'''
Implement the BSTIterator class that represents an iterator over the in-order 
traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The 
root of the BST is given as part of the constructor. The pointer should be 
initialized to a non-existent number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the 
right of the pointer, otherwise returns false.

int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the 
first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at 
least a next number in the in-order traversal when next() is called.

Constraints:
The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use 
O(h) memory, where h is the height of the tree?
'''

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BSTIterator:
	'''
		T = O(1)
		S = O(h) h = height of tree
	'''

	def __init__(self, root):
		# create a stack
		self.stack = []
		# fill stack with while iterating over all left child of node
		# as it is the same way how inorder proceed in background
		while root:
			self.stack.append( root )
			root = root.left

	def fillStack(self,node):
		# when ever we remove a node from stack we fill 
		# the remaining stack with the right root of current node 
		# node and all left child of the right node we got
		# 
		# it is because out aim is to keep minimum node of 
		# untraversed tree on top of stack always 
		if not node or not node.right:
			return 

		node = node.right
		while node:
			self.stack.append(node)
			node = node.left

	def next(self) -> int:
		node = self.stack.pop()
		self.fillStack(node)
		return node.val
		
	def hasNext(self) -> bool:
		# if there is still some node in stack then return true
		return len(self.stack) > 0

if __name__ == "__main__":
	root = TreeNode(8)
	root.left = TreeNode(6)
	root.right = TreeNode(10)
	l = root.left
	r = root.right 
	l.left = TreeNode(5)
	l.right =  TreeNode(7)
	r.left = TreeNode(9)
	r.right = TreeNode(11)

	# Your BSTIterator object will be instantiated and called as such:
	obj = BSTIterator(root)

	while obj.hasNext():
		print( obj.next() )