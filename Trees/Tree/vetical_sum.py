class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None


def vertical_sum_uilt(root,index,hash_table):
	if root is None:
		return None
	if index not in hash_table:
		hash_table[index] = 0
	
	hash_table[index] += root.data
	vertical_sum_uilt(root.left,index-1,hash_table)
	vertical_sum_uilt(root.right,index+1,hash_table)

def vertical_sum(root):
	hash_table = {}
	vertical_sum_uilt(root,0,hash_table)
	lst = []
	for i,v in hash_table.items():
		lst.append( (i,v) )
	lst.sort()
	return [b for a,b in lst]


if __name__ == "__main__":
	"""      root
		_____ 1______
		|			|
	____2____	____3____
	|		|	|		|
____4____	5	6		7
|		|
100		200
	"""
	root = Binary_Tree_Node(1)
	root.left = Binary_Tree_Node(2)
	root.right = Binary_Tree_Node(3)
	a = root.left
	b = root.right
	a.left = Binary_Tree_Node(4)
	a.right = Binary_Tree_Node(5)
	b.left = Binary_Tree_Node(6)
	b.right = Binary_Tree_Node(7)
	a.left.left = Binary_Tree_Node(100)
	a.left.right = Binary_Tree_Node(200)

	print( vertical_sum(root) )