import math
class TreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def fill_segment_tree(array,start,end,segment_tree,i):
	# here i is a parameter which indicate the current node of segment tree

	# if index range have only one element then make seg tree node 
	# and return its value to parent for making middle node 
	if start == end:
		segment_tree[i] = array[start]
		return segment_tree[i]

	mid = (start+end)//2

	l = fill_segment_tree(array,start,mid,segment_tree,2*i+1)
	r = fill_segment_tree(array,mid+1,end,segment_tree,2*i+2)
	# internal node is XOR of leaf nodes
	segment_tree[i] = l^r
	
	# return current segment tree node value
	return segment_tree[i]

def Segment_Tree(array):
	# calculate height of segment tree
	n = len(array)
	height = math.ceil( math.log(n,2) )

	# calculate max nodes required in seg tree 
	nodes_in_seg_tree = 2**(height+1) - 1

	# make a blank segment tree
	segment_tree = [None]*nodes_in_seg_tree

	# fill segment tree using given array
	fill_segment_tree(array,0,n-1,segment_tree,0)

	return segment_tree

def get_XOR(segment_tree,start,end,q_start,q_end,i):
	# if current node range is completely covered in query
	# return value of node
	if q_start <= start and end <= q_end:
		return segment_tree[i]
	
	# if query totally out of range return 0
	elif end < q_start or q_end < start:
		return 0  

	# if node range is partially under query then use some 
	# elements of left and some form right sub trees
	mid = (start+end)//2
	l = get_XOR(segment_tree,start,mid,q_start,q_end,2*i+1)
	r = get_XOR(segment_tree,mid+1,end,q_start,q_end,2*i+2)
	return l^r

def sub_update(segment_tree,start,end,index,diff,i):
	if index < start or end < index:
		return 
	
	segment_tree[i] = segment_tree[i] ^ diff

	# we need to reach leaf node until then we keep 
	# adding diff to all nodes in the path
	if start != end:
		mid = (start+end)//2
		sub_update(segment_tree,start,mid,index,diff,2*i+1)
		sub_update(segment_tree,mid+1,end,index,diff,2*i+2)

def update(array,st,i,value):
	n = len(array)
	diff = value ^ array[i]
	return sub_update(st,0,n-1,i,diff,0)


if __name__ == "__main__":
	# input array
	array = [1, 3, 5, 7, 9, 11]
	# get segment tree of array
	st = Segment_Tree(array)
	n = len(array)

	# get sum in between index 2 to 4, and = 5+7+9 = 21
	print( st )
	print( get_XOR(st,0,n-1,2,4,0) )

	# replace the value 7 at (0 based) index = 3 with value = 10 
	update(array,st,3,10)
	
	print(st)
	print( get_XOR(st,0,n-1,2,4,0) )

