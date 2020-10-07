from ast import NodeTransformer


class TSTNode:
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
		self.eq = None

class TST:
	def __init__(self,x = None):
		self.root = TSTNode(None)
		self.leaf = x

