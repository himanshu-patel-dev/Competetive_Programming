"""
Given two sorted arrays give the kth element after we merge them
T = O(logk)
S = O(1)	
"""
def kth_element(lst1,lst2,k):
	# if len of both list combined is less than k
	if len(lst2) + len(lst1) < k:
		return "Not enough elements"

	# let the first list be smaller
	if len(lst1) > len(lst2):
		lst2, lst1 = lst1, lst2

	# print(lst1,lst2,k)

	# first list len is zero return kth ele of second list 
	if len(lst1) == 0:
		return lst2[k-1]

	if k == 1:
		return min( lst1[0], lst2[0] )

	# get the k//2 th ele of both the list
	lst1_ele = lst1[k//2-1]
	lst2_ele = lst2[k//2-1]

	if lst1_ele < lst2_ele:
	# k//2 ele of lst1 are less than k//2 ele of lst2
	# cut loose the k//2 ele of lst1
		return kth_element(lst1[k//2:], lst2, k-k//2)
	else:
	# k//2 ele of lst2 are less than k//2 ele of lst1
	# cut loose the k//2 ele of lst2
		return kth_element(lst1, lst2[k//2:], k-k//2)
	

if __name__ == "__main__":
	lst1 = [2, 3, 6, 7, 9]
	lst2 = [1, 4, 8, 10]
	k = 5

	print( kth_element(lst1,lst2,k) )
