"""
n = no of nodes
m = no of union finf operations
T = O( (n+m)log(n) )
"""

class Union_Find:
	def __init__(self,n):
		self.Num_of_elements = n
		# initially there are n components which dec after each union operation
		self.Num_of_component = n
		self.MakeSet(n)

	def MakeSet(self,n):
		# n is the no of elements present in all the sets
		# initially all ele present in their own eq class 
		self.parent = 	[i for i in range(n)]
		# each component have size of 1 initially
		self.size = 	[1 for i in range(n)]

	def in_same_set(self,a,b):
		return self.Find(a) == self.Find(b)

	def Find(self,ele):
		# get the root of current element
		root = ele
		while root != self.parent[root]:
			root = self.parent[root]

		# assign every element in the path to root directly
		while ele != self.parent[ele]:
			ele, self.parent[ele] = self.parent[ele], root

		# return root
		return root

	def Union(self,x,y):
		# getting root of each element
		rootx = self.Find(x)
		rooty = self.Find(y)

		# already in same set
		if rootx == rooty:
			return

		# merge the component with smaller size into componenet of larger size
		if self.size[rootx] > self.size[rooty]:
			self.size[rootx] += self.size[rooty]
			self.parent[rooty] = rootx
		else:
			self.size[rooty] += self.size[rootx]
			self.parent[rootx] = rooty

		# a component get merged
		self.Num_of_component -= 1

if __name__ == "__main__":
	uf = Union_Find(5)

	print(uf.parent)
	print(uf.Find(3))
	uf.Union(0,2)
	print(uf.parent)
	uf.Union(2,3)
	print(uf.parent)
	print( uf.Find(0) )
