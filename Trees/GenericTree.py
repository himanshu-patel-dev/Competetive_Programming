class GenericTree:
	def __init__(self,value=None):
		self.value = value
		self.childList = []
		self.sibling = None

	def count_childern(self):
		return len(self.childList)

	def add_child(self,child):
		self.childList.append(child)

	def add_sibling(self,sibling):
		self.sibling = sibling

	def nth_child(self,n):
		if n > len(self.childList):
			return "out of index"
		else:
			return self.childList[n]

if __name__ == "__main__":
	"""
	
	"""
	root = GenericTree(1)
	root.add_sibling( GenericTree(2) )

	root.add_child( GenericTree(3) )
	root.add_child( GenericTree(4) )
	root.add_child( GenericTree(5) )

	root.sibling.add_child( GenericTree(6) )
	root.sibling.add_child( GenericTree(7) )
