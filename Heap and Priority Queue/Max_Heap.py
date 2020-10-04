class Max_Heap:
	def __init__(self):
		self.heap = []

	def get_parent(self,node):
		return (node-1)//2

	def get_left_child(self,node):
		return 2*node + 1

	def get_right_child(self,node):
		return 2*node + 2

	def has_parent(self,node):
		return (node-1)//2 >= 0

	def has_left_child(self,node):
		return 2*node+1 < len(self.heap)

	def has_right_child(self,node):
		return 2*node+2 < len(self.heap)

	# swap data of two nodes at index i and j
	def swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def insert_node(self,value):
		self.heap.append(value)
		# pass the index of node which we want to heapify
		self.heapify_up(len(self.heap)-1)

	def heapify_up(self,node):
		# loop until node have a parent
		while self.has_parent(node):
			# get the parent of current node
			parent = self.get_parent(node)
			# if parent smaller than child then swap the two
			# to maintain the max heap
			if self.heap[node] > self.heap[parent]:
				self.swap(node,parent)
				node = parent 
			else:
				break

	def print_heap(self):
		print(self.heap)

	# to get max element from max heap
	def delete_root(self):
		if len(self.heap) == 0:
			return None

		last_index = len(self.heap)-1
		# swap the root with last index element
		self.swap(0,last_index)
		# get the root
		root = self.heap.pop()

		# heapify down so that element at root reach at its position
		self.heapify_down(0)

		return root

	def heapify_down(self,node):
		# if left child is not present than right is also not present in 
		# heap as heap is a complete binary tree
		while self.has_left_child(node) or self.has_right_child(node):
			max_child_index = self.max_child(node)

			if max_child_index is None:
				break
			# put max child to parent position and point to new position
			if self.heap[node] < self.heap[max_child_index]:
				self.swap(node,max_child_index)
				node = max_child_index
			else:
			# if no child is greater than root than break
				break


	def max_child(self,node):
		left = right = None

		if self.has_left_child(node):
			left = self.get_left_child(node)

		if self.has_right_child(node):
			right = self.get_right_child(node)

		if left is None:
			return right

		if right is None:
			return left

		# return the index of max among two
		if self.heap[left] > self.heap[right]:
			return left
		else:
			return right	


	def get_min(self):
		n = len(self.heap)

		# min element if present is in leaf only
		# leaf start from element next to the parent of last node

		last_node = n-1				# index of last node
		parent = (last_node-1)//2	# index of its parent
		first_leaf = parent+1		# index of next to parent

		mi = float('inf')
		for i in range(first_leaf,n):
			mi = min(mi,self.heap[i])
		return mi

	def delete_element_i(self,i):
		# given index of an element delete it and maintain heap
		"""
		T = O(logn)
		S = O(1)
		"""

		n = len(self.heap)
		# index out of bound
		if i >= n:
			return None
		# move i th element to end
		self.swap(n-1,i)
		# pop the last element
		key = self.heap.pop()
		
		self.heapify_down(i)
		return key

	def find_and_delete(self,target):
		# find target in heap and delete from heap 
		# if found return True else return False

		""" T = O(n) a linear search """
		for i in range(len(self.heap)):
			if target == self.heap[i]:
				self.delete_element_i(i)
				return True
		return  False

	def merge_heap(self,new_heap):
		"""
		merge new_heap to current heap
		T = O((m+n)log(m+n))
		m = len(current heap) and n = len(new heap)
		"""
		# append heap2 at end of heap1
		self.heap.extend(new_heap.heap)

		n = len(self.heap)
		# iterating over all leaf nodes in final heap 
		# and heapify them all
		for i in range((n+1)//2,n):
			self.heapify_up(i)

	def K_th_max_element(self,k):
		"""
		return the kth max element from heap without deleting
		T = O(klogk)
		S = O(n)		# append all n ele to aux
		"""
		aux_heap = Max_Heap()

		mx_ele = None
		while k:
			mx_ele = self.delete_root()
			k -= 1
			aux_heap.insert_node(mx_ele)
		
		# now add remining original heap to aux heap 
		# just by extending
		aux_heap.heap.extend(self.heap)
		# assign the aux heap to current heap
		self.heap = aux_heap.heap

		return mx_ele

	def all_more_than_k_elements(self,k):
		"""
		give all elements of heap less than k
		without deleting them
		T = O(n)
		S = O(n)	recursive call
		"""
		def sub(node,n,res):
			if self.heap[node] > k:
				res.append(self.heap[node])
			
			left = 2*node+1
			right = 2*node+2

			if left < n:
				sub(left,n,res)
			if right < n:
				sub(right,n,res)
		
		res = []
		sub(0,len(self.heap),res)
		return res

def test_max_heap(max_heap):
	# make a deep copy of object so that 
	import copy
	h = copy.deepcopy(max_heap)

	lst1 = h.heap[:]
	lst1.sort(reverse=True)
	# print(lst1)

	lst2 = [] 
	while h.heap:
		lst2.append( h.delete_root() )

	if lst1 == lst2:
		print("Valid Max heap")
	else:
		print("Invalid Max Heap properties")

if __name__ == "__main__":
	lst = [45,99,63,27,29,57,42,35,12,24]

	max_heap = Max_Heap()
	for ele in lst:
		max_heap.insert_node(ele)

	# print("Insert node in Heap")
	# max_heap.insert_node(50)
	# max_heap.print_heap()

	# print("Delete node from Heap")
	# print("Max Element: ", max_heap.delete_root())
	# max_heap.print_heap()

	# print("Get the min element in max heap: ", max_heap.get_min())


	# make a new heap and merge with older one
	# lst = [1,2,3,4,5]
	# mx_heap = Max_Heap()
	# for e in lst:
	# 	mx_heap.insert_node(e)
	# print( test_max_heap(max_heap) )

	# max_heap.merge_heap(mx_heap)
	# max_heap.print_heap()

	print("3rd max element: ", max_heap.K_th_max_element(3) )

	print(max_heap.all_more_than_k_elements(40))

	# testing heap property after all operations
	test_max_heap(max_heap)
	max_heap.print_heap()