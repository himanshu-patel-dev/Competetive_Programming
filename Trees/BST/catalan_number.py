class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def catalan(n):
	""" number of structurally different BST that can be made from n nodes """
	if n <= 1:
		return 1
	sums = 0
	for root in range(1,n+1):
		left = catalan(root-1)
		right = catalan(n-root)
		sums += left * right
	return sums

def catalan_fast(n):
	from math import factorial

	num = factorial(2*n)
	den_1 = factorial(n)
	den_2 = factorial(n+1)

	return num//(den_1*den_2)

if __name__ == "__main__":
	print( catalan(8) )
	print( catalan(8) )
