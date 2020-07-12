"""
performing range query of inc or dec by k in O( 1 ) time and for each query
and making final sum in O(n) time. 
total comp = O(n)
"""

for _ in range(int(input())):
	n,k = list(map(int, input().split()))	# no of elements and no of query
	lst = [0]*(n+1)		# initial array of elements ( all zeros )
	for i in range(k):
		l,r,inc = list(map(int, input().split()))	# left index , right index, inc amount
		lst[l] += inc
		lst[r+1] -= inc
	for i in range(1,n+1):
		lst[i] += lst[i-1]
	print(max(lst[:-1]))

"""
2
5 3
0 1 100
1 4 100
2 3 100
4 3
1 2 603
0 0 286
3 3 882
"""