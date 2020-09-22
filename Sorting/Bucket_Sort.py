"""
Bucket sort
T = O(n^2) ..worst 
T = O(n)...best
S = O(n)
"""

def Insertion_Sort(lst):
	for i in range(1,len(lst)):
		temp = lst[i]
		j = i
		while j > 0 and lst[j-1] > temp:
			lst[j] = lst[j-1]
			j -= 1
		lst[j] = temp

def Bucket_sort(lst):
	# one bucket for each 0 to 9 
	Buckets = [ [] for i in range(10)]

	# considering all elements in range 0 to 1
	# map all of then to respective bucket based on first digit after decimal
	for ele in lst:
		b = int(10*ele)
		Buckets[b].append(ele)

	# sort all buckets using insertion sort
	for bucket in Buckets:
		Insertion_Sort(bucket)

	# Output the elements from buckets to original list
	k = 0 	
	for bucket in Buckets:
		for ele in bucket:
			lst[k] = ele
			k += 1

	return lst

if __name__ == "__main__":
	lst = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434, 0.121, 0.158, 0.864]  
	print( Bucket_sort(lst) )
