import heapq

class Median_Heap:
	def __init__(self):
		# note: heapq make a min heap thus make a max 
		# heap use -ve of element value
		self.Max_Heap = []	# left
		self.Min_Heap = []	# right

	def insert_element(self,ele):
		# if both heap are empty then append to min heap
		if not self.Min_Heap and not self.Max_Heap:
			heapq.heappush(self.Min_Heap,ele)

		# if max heap is empty compare based on min heap
		elif not self.Min_Heap:
			# ele less than root of max heap push it to max heap 
			# beacause if it cause any imbalance in max heap then 
			# root (higher then ele) will get shifted to min heap 
			if ele < -self.Max_Heap[0]:
				heapq.heappush(self.Max_Heap,-ele)

			# otherwise push it to min heap as it will any how 
			# appear as root of max heap
			else:
				heapq.heappush(self.Min_Heap,ele)
		
		# if max heap is empty then compare based on min heap
		elif not self.Max_Heap:
			if ele > self.Min_Heap[0]:
				heapq.heappush(self.Min_Heap,ele)
			else:
				heapq.heappush(self.Max_Heap,-ele)

		# if both are non empty use any - lets use max heap
		else:
			if ele < -self.Max_Heap[0]:
				heapq.heappush(self.Max_Heap,-ele)
			else:
				heapq.heappush(self.Min_Heap,ele)

		# balance both the heaps if they differ by more than
		# one element in size, at any point they do not differ 
		# by by more than two elements
		min_len = len(self.Min_Heap)
		max_len = len(self.Max_Heap)

		if abs( min_len - max_len ) > 1:
			if min_len > max_len:
				ele = heapq.heappop(self.Min_Heap)
				heapq.heappush(self.Max_Heap,-ele)
			else:
				ele = -heapq.heappop(self.Max_Heap)
				heapq.heappush(self.Min_Heap,ele)
			
	def get_median(self):
		min_len = len(self.Min_Heap)
		max_len = len(self.Max_Heap)
		# print(self.Max_Heap,self.Min_Heap)

		if min_len == max_len:
			# note the value obtained from max heap is -ve
			return (self.Min_Heap[0]-self.Max_Heap[0])/2
		elif min_len > max_len:
			return self.Min_Heap[0]
		else:
			return self.Max_Heap[0]


if __name__ == "__main__":
	lst = [1,2,10,7,14,6]

	median_heap = Median_Heap()

	for ele in lst:
		print('Current ele: ',ele)
		median_heap.insert_element(ele)
		print( 'Media: ',median_heap.get_median() )
		print()