'''
You are given the root of a binary search tree (BST), where exactly two 
nodes of the tree were swapped by mistake. Recover the tree without 
changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. 
Could you devise a constant space solution?
'''

class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.val = data
		self.right = None
		self.left = None

def make_tree():

	"""      root
		_____ 10______
		|			 |
	____18___	 ____5___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = BST_Tree_Node(10)
	root.left = BST_Tree_Node(18)
	root.right = BST_Tree_Node(5)
	a = root.left
	b = root.right
	a.left = BST_Tree_Node(3)
	a.right = BST_Tree_Node(7)
	b.left = BST_Tree_Node(16)
	b.right = BST_Tree_Node(20)
	a.left.left = BST_Tree_Node(2)

	# 18 and 5 have been misplaced

	return root

def inorder(root,res):
	if not root:
		return

	inorder(root.left,res)
	res.append(root.val)
	inorder(root.right,res)
	return res


'''
There can be two main cases:
1. We have 1, 2, 3, 4, 5 and swapped nodes are adjacent, 
for example 1, 2, 4, 3, 5. In this case, we have only one 
oddity: 4 and 3: and we save them to our cands list. And we need 
to change values for the first and for the last nodes in our cands.

2. We have 1, 2, 3, 4, 5 and swapped nodes are not adjacent, 
for example 1, 2, 5, 4, 3. In this case we have two 
oddities: 5 and 4; 4 and 3. In this case we again need to swap the 
first and the last nodes.
'''
class Solution:
	def recoverTree(self, root):
		"""
		Do not return anything, modify root in-place instead.
		"""
		self.first = None
		self.second = None
		self.prev = None

		self.get_swapped_nodes(root)
		self.first.val, self.second.val = self.second.val, self.first.val

	def get_swapped_nodes(self,root):
		if not root:
			return

		self.get_swapped_nodes(root.left)
		
		if self.prev:
			# inorder successor is less than inorder predicessor
			if root.val < self.prev.val:
				# if this is hapenning first time
				if self.first is None:
					# prev node of higher value is swapped node
					self.first = self.prev
				
				# if this happed only for one time when swapped nodes are 
				# adjacent in inorder traversal then assign second node also
				
				# else when it happens second time then second node of 
				# lower value is the swapped node 
				self.second = root
		# assign current node to previou before moving to next node
		self.prev = root

		self.get_swapped_nodes(root.right)


if __name__ == "__main__":
	s = Solution()
	root = make_tree()
	# notice the inorder is not sorted
	print("Inorder: ", inorder(root,[]) )
			
	# recover the original BST
	s.recoverTree(root)
		
	# check the inorder again
	print("Inorder: ", inorder(root,[]) )