"""
find the index where lst[i] = i and given list is sorted and have 
T = O(log(n))
"""
def FixedPoint(lst,start,end):
	if start > end:
		return -1

	mid = (start+end)//2

	if mid == lst[mid]:
		return mid
	
	if mid > lst[mid]:
		return FixedPoint(lst,mid+1,end)
	else:
		return FixedPoint(lst,start,mid-1)
	# return -1 if not found
	return -1

if __name__ == "__main__":
	lst = [-10, -5, 0, 3, 7]
	print( FixedPoint(lst,0,len(lst)-1) )

	lst = [0, 2, 5, 8, 17]
	print( FixedPoint(lst,0,len(lst)-1) )