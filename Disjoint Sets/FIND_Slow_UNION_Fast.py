"""
Fast FIND 		T = O(N)
Slow UNION 		T = O(1)
"""

class Union_Find:
	def __init__(self,n):
		self.MakeSet(n)

	def MakeSet(self,n):
		# n is the no of elements present in all the sets
		# initially all ele present in their own eq class 
		self.parent = [i for i in range(n)]

	def Find(self,ele):
		if self.parent[ele] == ele:
			return ele
		else:
			return self.Find( self.parent[ele] )

	def Union(self,x,y):
		self.parent[x] = y


if __name__ == "__main__":
	uf = Union_Find(5)

	print(uf.parent)
	print(uf.Find(3))
	uf.Union(0,2)
	uf.Union(2,3)
	print(uf.parent)
	print( uf.Find(0) )
