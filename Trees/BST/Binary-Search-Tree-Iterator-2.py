"""
https://leetcode.com/problems/binary-search-tree-iterator-ii/
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. 
The pointer should be initialized to a non-existent number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

int next() Moves the pointer to the right, then returns the number at the pointer.

boolean hasPrev() Returns true if there exists a number in the traversal to the left of the pointer, otherwise returns false.

int prev() Moves the pointer to the left, then returns the number at the pointer.
"""

class TreeNode:
	def __init__(self,data):
		self.val = data
		self.right = None		# points to forward node
		self.left = None		# points to backward node

class BSTiterator:
	def __init__(self,root):
		self.head = None
		self.tail = None
		self.BSTtoDLL(root)
		self.dummyHead = TreeNode(-1)
		self.head.left, self.dummyHead.right = self.dummyHead, self.head

		self.head = self.dummyHead

	def BSTtoDLL(self, root):
		if not root:
			return

		self.BSTtoDLL(root.left)

		if not self.head:
			# this exec one time only of left most node
			self.head = root
		else:
			# this exec on every node except left most node
			root.left = self.tail
			self.tail.right = root
		
		# before leaving this root mark is as tail
		self.tail = root
		
		self.BSTtoDLL(root.right)

	def printlist(self):
		while self.hasNext():
			print(self.next(), end=', ')
		print()

		while self.hasPrev():
			print(self.prev(), end=', ')
		print()

	def next(self):
		self.head = self.head.right
		return self.head.val

	def hasNext(self):
		return bool(self.head.right)

	def prev(self):
		prev = self.head
		self.head = self.head.left
		return prev.val
	
	def hasPrev(self):
		return bool(self.head.left)


if __name__ == "__main__":
	"""
			 root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = TreeNode(10)
	root.left = TreeNode(5)
	root.right = TreeNode(18)
	a = root.left
	b = root.right
	a.left = TreeNode(3)
	a.right = TreeNode(7)
	b.left = TreeNode(16)
	b.right = TreeNode(20)
	a.left.left = TreeNode(2)

	iterator = BSTiterator(root)
	iterator.printlist()
