"""
Fast FIND 		T = O(1)
Slow UNION 		T = O(N)
"""

class Union_Find:
	def __init__(self,n):
		self.n = n
		self.MakeSet(n)

	def MakeSet(self,n):
		# n is the no of elements present in all the sets
		# initially all ele present in their own eq class 
		self.parent = [i for i in range(n)]

	def Find(self,ele):
		return self.parent[ele]

	def Union(self,a,b):
		i = self.Find(a)
		j = self.Find(b)

		for k in range(self.n):
			if self.parent[k] == i:
				self.parent[k] = j

if __name__ == "__main__":
	uf = Union_Find(5)

	print(uf.parent)
	print(uf.Find(3))
	uf.Union(0,2)
	print(uf.parent)
