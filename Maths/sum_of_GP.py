def sum_of_GP(n,a,r):
	""" n = no of terms, a = first term, r = common ratio """
	if r == 1:
		return a*n
	return a * ((r**n)-1)//(r-1)

if __name__ == "__main__":
	for _ in range(int(input())):
		n = int(input())
		a,r = map(int, input().split() )
		print( sum_of_GP(n,a,r) )