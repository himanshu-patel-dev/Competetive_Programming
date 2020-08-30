"""
Replace every element with the next greatest element 
(greatest element on its right side) in the array. Also, 
since there is no element next to the last element, replace 
it with -1.
"""

def next_greatest(lst,n):
	prev_largest = -1

	for i in range(n-1,-1,-1):
		temp = lst[i]
		lst[i] = prev_largest
		prev_largest = max(prev_largest, temp)
	return lst

if __name__ == "__main__":
	n = 6
	lst = [16,17,4,3,5,2]
	print( next_greatest(lst,n) )

