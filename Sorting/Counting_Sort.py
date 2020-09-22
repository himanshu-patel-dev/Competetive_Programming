"""
Counting sort
T = O(K+n) ..worst, T = O(n)...best
S = O(K+n)
"""

def Counting_sort(lst):
	n = len(lst)
	mx = max(lst)+1
	# zero based index
	count = [0]*mx

	# count occurace of all decision
	for ele in lst:
		count[ele] += 1

	# for each element count no of ele below it
	for index in range(1,mx):
		count[index] += count[index-1]

	result = [0]*n
	for ele in lst:
		# no of ele below current ele are one less than total 
		# ele less than and ele itself count we calculated 
		pos = count[ele]-1
		result[pos] = ele

	return result

if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]

	print( Counting_sort(lst) )