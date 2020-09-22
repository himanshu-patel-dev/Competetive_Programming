"""
Radix sort
n = len of list, w = max no of digit in among all elements
T = O(nw) ..worst, 
T = O(nw) ..best
S = O(n)
"""

def Counting_sort(lst,exp):
	n = len(lst)
	count = [0]*10
	result = [0]*n

	# mapping each ele based on its digit to count
	for ele in lst:
		# getting the required digit for sorting
		index = (ele//exp)%10
		count[index] += 1

	# now for each ele get how many ele are below it
	for i in range(1,10):
		count[i] += count[i-1]

	# traverse the array from end in this way the ele who already get sorted 
	# will probe their position in end and will get remaped to same position
	# while the ele with more no of digits will get mapped to end of array
	for ele in lst[::-1]:
		digit = (ele//exp)%10
		pos = count[digit]-1
		result[pos] = ele
		# dec count by 1
		count[digit] -= 1
	# print('+',result)
	return result

def Radix_Sort(lst):
	# starting with last bit of each number
	exp = 1
	mx = max(lst)

	while mx//exp > 0:
		lst = Counting_sort(lst,exp)
		# to choose digit one left to current level
		exp = exp*10
	return lst

if __name__ == "__main__":
	lst = [3,6,4,7,1,128,9,2,55]
	print( Radix_Sort(lst) )
