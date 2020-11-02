'''
Given an array of 2n char a1 a2 a3 b1 b2 b3

Swap the ele in such a way that a1 b1 a2 b2 a3 b3

T = O(n) and S = O(1)
'''

def pattern(lst):
	n = len(lst)

	if n <= 2:
		return lst

	# divide the actual part in 
	left = lst[:n//2]
	right = lst[n//2:]

	l,r = len(left), len(right)

	left, right = left[:l//2] + right[:r//2], left[l//2:] + right[r//2:]

	left = pattern(left)
	right = pattern(right)
	return left+right

if __name__ == "__main__":
	lst = ['a1','a2','a3','a4','b1','b2','b3','b4']
	print( pattern(lst) )

	lst = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
	print( pattern(lst) )