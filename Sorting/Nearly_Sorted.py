"""
Nearly Sorted Array means in given array each element is displaced at most 
k distance from its original distance

T = O(nlogk)
S = O(k)

Take a priority queue of size k and slide it as a window and at each index pop 
the mini element and input the K+1 the element
"""

from bisect import insort

def Nearly_Sorted(lst,k):
	n = len(lst)
	# diff btw first and last element index are of K atmost
	priority_queue = lst[:k+1]
	priority_queue.sort()
	result = [0]*n

	# n - (k+1) + 1 = n-k
	for i in range(n-k-1):
		# print(i)
		result[i] = priority_queue.pop(0)
		# enter next element into priority queue
		insort(priority_queue,lst[i+k+1])

	i += 1
	while i<n:
		result[i] = priority_queue.pop(0)
		i += 1

	return result

if __name__ == "__main__":
	lst1 = [4,3,5,1,2,7,6]
	print( Nearly_Sorted(lst1,3) )

	# give incorrect result as repeated element are not considered
	lst2 = [1,3,4,0,2,2,1,5,7,6]
	print( Nearly_Sorted(lst2,5) )