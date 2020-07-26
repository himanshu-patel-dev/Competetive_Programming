class GenericTree:
	def __init__(self,data=None):
		self.data = data
		self.childList = []
		self.sibling = None

	def add_child(self,child):
		if len(self.childList) > 0:
			self.childList[-1].sibling = child
		self.childList.append(child)

def sum_all_nodes(root):
	if root is None:
		return 0
	s = root.data
	for c in root.childList:
		s += sum_all_nodes(c)
	return s

def count_nodes(root):
	if root is None:
		return 0
	count = 1
	for c in root.childList:
		count += count_nodes(c)
	return count

def count_sibling(root):
	if root is None:
		return 0
	c = 0
	t = root
	while t:
		c += 1
		t = t.sibling
	return c


if __name__ == "__main__":
	"""
		   ______50_____
		   |		   |
		___1___    ____2___
		|  |  |    |	  |
		3  4  5	   6  ____7_____
					  |  |  |  |
					  9  10 11 12	
	"""

	root = GenericTree(50)
	root.add_child( GenericTree(1) )
	root.add_child( GenericTree(2) )
	a = root.childList[0]
	b = root.childList[1]

	a.add_child( GenericTree(3) )
	a.add_child( GenericTree(4) )
	a.add_child( GenericTree(5) )

	b.add_child( GenericTree(6) )
	b.add_child( GenericTree(7) )

	x = b.childList[1]
	x.add_child( GenericTree(9) )
	x.add_child( GenericTree(10) )
	x.add_child( GenericTree(11) )
	x.add_child( GenericTree(12) )

	# total sum = 120
	print( sum_all_nodes(root) )
	# total nodes = 12
	print( count_nodes( root ) )
	# total sibling = 4
	print( count_sibling( x.childList[0] ) )
