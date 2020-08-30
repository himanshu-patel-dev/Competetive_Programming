"""
increment(a, b, k) : Increment values from 'a' to 'b' by 'k'.  
After M operations, calculate the maximum value in the array.
"""

for _ in range(int(input())):
	n,m = map(int, input().split())
	lst = [0]*(n+1)

	for i in range(m):
		# both a and b are zero index
		a,b,k = map(int, input().split())
		lst[a] += k
		lst[b+1] -= k

	for i in range(1,n):
		lst[i] += lst[i-1]
	lst = lst[:n]

	# print(lst)
	print(max(lst))