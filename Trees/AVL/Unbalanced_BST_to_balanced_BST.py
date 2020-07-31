class AVL_TreeNode:
	""" AVL Node """
	def __init__(self,data):
		self.data 	= data
		self.bf 	= None		# balance factor
		self.right 	= None
		self.left 	= None


def Inorder(root,result):
	if root is None:
		return None

	Inorder(root.left,result)
	result.append( root.data )
	Inorder(root.right,result)

	return result

def Make_Balanced_Tree(lst,start,end):
	""" take a sorted array and make a balanced BST form it """
	if start > end:
		return None

	mid = (start + end)//2
	node = AVL_TreeNode(lst[mid])
	node.left = Make_Balanced_Tree(lst,start,mid-1)
	node.right = Make_Balanced_Tree(lst,mid+1,end)
	return node

def Convert_to_balanced_BST(root):
	inorder = Inorder(root,[])
	n = len(inorder)
	return Make_Balanced_Tree(inorder,0,n-1)


if __name__ == "__main__":
	"""
		  root
		___4
		|	
	____2
	|		
    1		

		root
	  ___2___
	  |		|
	  1 	4

	"""

	root = AVL_TreeNode(4)
	root.left = AVL_TreeNode(2)
	root.left.left = AVL_TreeNode(1)

	root = Convert_to_balanced_BST(root)

	print(root.left.data, root.data, root.right.data)
