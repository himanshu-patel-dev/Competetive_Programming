"""
Given an unsorted array arr of size N, rearrange the elements of array 
such that number at the odd index is greater than the number at the 
previous even index. All elements may not be distinct
"""

def formatArray(lst,n):
	lst.sort()
	result = []

	if n%2 == 0:
		# divide into half
		first = lst[:n//2]
		sec = lst[n//2:]
	else:
		# leave middle ele and divide into half
		first = lst[:n//2]
		sec = lst[n//2+1:]
	
	# for n ele there are n//2 comparison
	valid = True
	for i in range(n//2):
		if first[i] >= sec[i]:
			valid = False
			break
		result.append(first[i])	# even index
		result.append(sec[i])	# odd index

	print(valid)
	# if odd len append middle ele in end, as last ele 
	# have even index and not compared to its right anymore
	if n%2 != 0:
		result.append(lst[n//2]) 
	# if valid print array
	if valid:
		print(result)
		
if __name__ == "__main__":
	lst = [1,2,3,3,4,5]
	formatArray(lst,len(lst))

	lst = [1,2,3,3,4,5,4]
	formatArray(lst,len(lst))