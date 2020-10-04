"""
You have k lists of sorted integers in non-decreasing order. Find the 
smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c 
or a < c if b - a == d - c.
"""
############################## Approch 1 #####################################

import heapq

class Solution:
	""" 
	T = O(n*logk)
	S = O(k) 
	n = total no of ele including all k arrays
	k = no of lists
	"""
	def smallestRange(self, nums):
		# form a min heap of k ele one from each array
		heap_list = [ (lst[0],0,i) for i,lst in enumerate(nums)]
		heapq.heapify(heap_list)

		# get the min and max ele from a heap
		mi = min(heap_list, key = lambda x: x[0])
		mx = max(heap_list, key = lambda x: x[0])

		# tuple to int
		mx,mi = mx[0], mi[0]
		# variable to hold max ele of min heap so that we sont have 
		# to search entire heap for max ele each time
		curr_mx = mx

		# loop until the no of ele in heap is equal to k
		# one from each array 
		while len(heap_list) == len(nums):
			# this ele changes the min of range
			ele, ele_index, list_index = heapq.heappop(heap_list)

			# range is mx-mi beacause mx change with push of each 
			# ele if new element push is greater than mx also ele is
			# smallest ele in heap
			if curr_mx-ele < mx-mi:		# range = mx - mi
				mx,mi = curr_mx, ele		# update the range to min possible

			ele_index += 1

			# each of the k array can have different value
			# for deleted min ele we fetch new ele from same list
			# at any point of time there are k ele from each arrray
			if ele_index < len(nums[list_index]):
				new_ele = nums[list_index][ele_index]
				curr_mx = max(curr_mx,new_ele)	# this changes the mx for range
				heapq.heappush(heap_list, (new_ele,ele_index,list_index) )

		return [mi,mx]

############################## Approch 2 #####################################

class Node:

	def __init__(self, key, ele_index, list_index):
		self.key = key
		self.i = ele_index
		self.l_i = list_index

	# compares the second value
	def __lt__(self, other):
		return self.key < other.key

	def __str__(self):
		return self.key

class Solution:
	""" 
	T = O(n*logk)
	S = O(k) 
	n = total no of ele including all k arrays
	k = no of lists
	"""
	def smallestRange(self, nums):
		# form a min heap of k ele one from each array
		heap_list = [ Node(lst[0],0,i) for i,lst in enumerate(nums)]
		heapq.heapify(heap_list)

		# get the min and max ele from a heap
		mi = min(heap_list, key = lambda x: x.key)
		mx = max(heap_list, key = lambda x: x.key)

		# object to int
		mx,mi = mx.key, mi.key
		# variable to hold max ele of min heap so that we sont have 
		# to search entire heap for max ele each time
		curr_mx = mx

		# loop until the no of ele in heap is equal to k
		# one from each array 
		while len(heap_list) == len(nums):
			# this ele changes the min of range
			node = heapq.heappop(heap_list)
			ele, i, l_i = node.key, node.i, node.l_i

			# range is mx-mi beacause mx change with push of each 
			# ele if new element push is greater than mx also ele is
			# smallest ele in heap
			if curr_mx-ele < mx-mi:		# range = mx - mi
				mx,mi = curr_mx, ele		# update the range to min possible

			i += 1

			# each of the k array can have different value
			# for deleted min ele we fetch new ele from same list
			# at any point of time there are k ele from each arrray
			if i < len(nums[l_i]):
				new_ele = nums[l_i][i]
				curr_mx = max(curr_mx,new_ele)	# this changes the mx for range
				heapq.heappush(heap_list, Node(new_ele,i,l_i) )

		return [mi,mx]

if __name__ == "__main__":
	s = Solution()

	nums = [
		[4,10,15,24,26],
		[0,9,12,20],
		[5,18,22,30]
	]
	print( s.smallestRange(nums) )

	nums = [
		[1,2,3],
		[1,2,3],
		[1,2,3]
	]
	print( s.smallestRange(nums) )
