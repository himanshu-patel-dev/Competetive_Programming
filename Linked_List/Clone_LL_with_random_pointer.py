def print_list(head,flag=0):

	if flag == 0:
		# print entire linked list with next
		while head.next != None:
			print(head,' -> ',end='')
			head = head.next
		print(head.data)
	else:
		# print entire linked list with random links
		while head != None:
			print(head,'-',head.random,end=', ')
			head = head.next
		print()

class Node:
	def __init__(self,data) -> None:
		self.data = data
		self.next = None
		self.random = None

	def __str__(self) -> str:
		return str(self.data)


def CloneLL(head):
	''' 
	Return a clone of LL with next and random pointer 
	T = O(n)
	S = O(n)
	'''
	hash = {}
	# hash all new node as value with original node as key
	t = head
	while t:
		hash[t] = Node(t.data)
		t = t.next

	# link all nodes in clone with random pointer
	t = head
	while t:
		a,b = t, t.random
		if a and b:
			hash[a].random = hash[b]
		t = t.next

	# link all nodes in clone map with next pointer
	clone = Node(0)
	sec = clone
	first = head
	while first:
		sec.next = hash[first]
		sec = sec.next
		first = first.next
	clone = clone.next

	return clone


def CloneLL(head):
	''' 
	Return a clone of LL with next and random pointer 
	T = O(n)
	S = O(1)
	'''
	t = head
	# insert a dummy node after each of the original node with 
	# same data as original node
	while t:
		newNode = Node(t.data)
		newNode.next = t.next
		t.next = newNode
		# next to next node
		t = t.next.next

	# create the random link in bw new nodes
	t = head
	while t:
		# get the node and its random node 
		a,b = t, t.random
		# get corresponding nodes from new LL
		new_a,new_b = a.next, b.next
		# create random link bw two
		new_a.random = new_b
		t = t.next.next

	# seperate new LL with old LL in linear time
	t = head
	clone = Node(None)	# let head be a blank node
	new = clone			# iterator for new LL
	while t:
		# add node in new LL and remove this new node from old LL
		new.next, t.next = t.next, t.next.next
		# repeat for all other old node in old LL
		t = t.next
		new = new.next
	# remove first blank node in new LL
	clone = clone.next
	
	# print_list(head,0)
	# print_list(clone,0)
	return clone

 
if __name__ == "__main__":
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)
	# crate next link
	a.next, b.next, c.next, d.next = b,c,d,e 
	# crete random link
	a.random = c
	c.random = e
	e.random = b
	d.random = c
	b.random = a
	# print LL
	print("---------------Original---------------")
	print('Next: ',end=' ')
	print_list(a,0)
	print('Random Links: ',end=' ')
	print_list(a,1)
	print("-----------------Clone-----------------")
	clone = CloneLL(a)
	print('Next: ',end=' ')
	print_list(clone,0)
	print('Random Links: ',end=' ')
	print_list(clone,1)