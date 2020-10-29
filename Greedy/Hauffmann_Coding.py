import heapq

class TreeNode:
	def __init__(self,key=None,freq=0):
		self.key = key
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self,other):
		return self.freq < other.freq

	def __str__(self):
		return str("{} : {}".format(self.key, self.freq))

	@staticmethod
	def merge(node1,node2):
		newNode = TreeNode(freq=node1.freq+node2.freq)
		newNode.left = node1	
		newNode.right = node2
		return newNode

def inorder(root,codes,seq):
	if not root:
		return

	inorder(root.left,codes,seq+'0')
	if root.key:
		codes[root.key] = seq
	inorder(root.right,codes,seq+'1')

def hauffman_coding(lst):
	# make a min heap
	lst = [ TreeNode(tup[0],tup[1]) for tup in lst]
	heapq.heapify(lst)

	while len(lst) > 1:
		a = heapq.heappop(lst)
		b = heapq.heappop(lst)
		# push the merge node
		heapq.heappush(lst,TreeNode.merge(a,b)) 

	# final node is the root node of hauffman tree
	Tree = lst[0]

	# make a inorder traversal of tree and get code of all char in list
	codes = {}
	inorder(Tree,codes,"")
	return codes

if __name__ == "__main__":
	lst = [ ('a',12), ('c',7), ('b',2), ('e',14), ('f',85), ('d',13) ]
	coding = hauffman_coding(lst)
	for k,code in coding.items():
		print(k,code)