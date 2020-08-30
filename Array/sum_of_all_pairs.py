"""
Given an array A of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) 
such that (1 <= i < j <= n).
If | a[j]-a[i] | > 1
	f(a[i], a[j]) = a[j] - a[i]
Else  if | a[j]-a[i] | <= 1
	f(a[i], a[j]) = 0

that is add pair wise sum (+ or -) only if abs diff > 1 among lst[i] and lst[j]
"""

from collections import defaultdict

def pair_sum(lst,n):
	result = 0
	cum_sum = 0
	count = defaultdict(int) 

	for i in range(n):
		# add to total i times current value - summulative sum of all previous value
		# as we need to get lst[j] - lst[i] for all pairs from 0 to i
		# lst[2] - lst[1] + lst[2] - lst[0] ===> 2*lst[2] - lst[1] - lst[0] 
		result += i*lst[i] - cum_sum
		# update cumm sum
		cum_sum += lst[i]

		# if lst[i]-1 is already present the we have added 
		# lst[i] - (lst[i]-1) ==> 1 to result extra
		if (lst[i]-1) in count:
			result -= count[ lst[i]-1 ]

		# if lst[i]+1 is already present the we have added 
		# lst[i] - (lst[i]+1) ==> -1 to result extra
		if (lst[i]+1) in count:
			result += count[ lst[i]+1 ]

		# count current element
		count[lst[i]] += 1
	return result

if __name__ == "__main__":
	n = 4
	lst = [6,6,4,4]
	print( pair_sum(lst,n) )

	n = 5
	lst = [1,2,3,1,3]
	print( pair_sum(lst,n) )