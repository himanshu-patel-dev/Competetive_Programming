class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None		# points to forward node
		self.left = None		# points to backward node

def inorder_BST(root,inorder):
	if root is None:
		return
	inorder_BST(root.left, inorder)
	inorder.append(root.data)
	inorder_BST(root.right, inorder)
	return inorder

def print_list(head):
	while head.right:
		print(head.data,end=' -> ')
		head = head.right
	print(head.data)

def get_middle(head):
	""" 
	return middle element in odd len DLL
	and sec half first node in even len DLL
	"""
	a = b = head
	while b.right and b.right.right:
		b = b.right.right
		a = a.right
	if b.right:
		a = a.right
	return a

def DLL_to_BST(head):
	""" take head of Double linked list and return root of balanced BST """
	if head is None or head.right is None:
		return head
	
	mid = get_middle(head)
	first = head

	# for LST
	while first.right != mid:
			first = first.right
	first.right = None
	mid.left = DLL_to_BST(head)

	# for RST
	if mid.right:
		second = mid.right
		second.left = None
		mid.right = DLL_to_BST(second)
	else:
		mid.right = None
	
	return mid
	

if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	head = BST_Tree_Node(2)
	lst = [3,5,7,10,16,18,20]
	temp = head
	for ele in lst:
		n = BST_Tree_Node(ele)
		temp.right = n
		n.left = temp
		temp = n

	print_list(head)
	root = DLL_to_BST(head)
	print( inorder_BST(root,[]) )