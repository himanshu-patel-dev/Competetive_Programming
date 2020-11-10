class Node:
	# constructor for single node
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

class LL_Tools:

	@staticmethod
	def length(head):
		# gettting length of linked list
		count = 0
		while head != None:
			count += 1
			head = head.next
		return count

	@staticmethod
	def print_list(head):
		# print entire linked list
		while head.next != None:
			print(head.data,' -> ',end='')
			head = head.next
		print(head.data)

	@staticmethod
	def del_value(head,value):
		# deleting node by its value (only first occurance of value)
		current = head
		previous = head

		# if head need to be deleted
		if current.data == value:
			return current.next

		while current.next != None and current.data != value:
			previous, current = current, current.next

		# if value is found it is deleted else nothing happens
		if current.data == value:
			previous.next = current.next
		# return the updated LL
		return head

	@staticmethod
	def insert_beginning(head,data):
		# inserting node at beginning
		newNode = Node(data)
		newNode.next = head
		return newNode

	@staticmethod
	def insert_end(head,data):
		# inserting node at end
		newNode = Node(data)

		if not head:
			return newNode

		t = head
		while t.next != None:
			t = t.next
		# no need to return any thinf the LL passed as argument is itself modified
		t.next = newNode
		return head

	@staticmethod
	def insert_after_k(head,k,data):
		# insert at k th location (head is at location 0 and end at location n)
		l = LL_Tools.length(head)

		if k < 0 or k > l:
			print("Not proper index")
			return None
		elif k == 0:
			return LL_Tools.insert_beginning(head,data)
		elif k == l:
			return LL_Tools.insert_end(head,data)
		
		res = head
		newNode = Node(data)
		count = 0
		while count < k-1:	# zero based indexing
			count += 1
			head = head.next
		
		newNode.next = head.next
		head.next = newNode
		return res

	@staticmethod
	def del_beginning(head):
		if head is not None:
			head = head.next
		return head

	@staticmethod
	def del_last(head):
		# delete last element of list
		if head is None:
			raise "Head is None"

		previous_node = None
		current_node = head

		while current_node.next != None:
			previous_node, current_node = current_node, current_node.next
		previous_node.next = None

	@staticmethod
	def del_node(head,node):
		# deleting node by its reference passed
		if head is None:
			raise "Head is None"

		current = head
		previous = None
		found = False

		while not found:
			if current == node:
				found = True
			elif current is None:
				raise ValueError("Node not found")
			else:
				previous = current
				current = current.next

		if previous is None:
			head = current.next
		else:
			previous.next = current.next

	@staticmethod
	def kth_node_from_end(head,k):
		# first start a pointer and move it k step forward
		# then start moving other pointers till first pointer each end
		first = head
		while first and k:
			first = first.next
			k -= 1

		if k>0:
			raise 'Less than k nodes in Linked List'

		second = head
		while first:
			first = first.next
			second = second.next

		return second.data

	@staticmethod
	def reverse_LL(head):
		curr, prev = head, None
		while curr:
			curr.next, curr, prev = prev, curr.next, curr
		return prev

	@staticmethod
	def find_intersect(head1,head2):
		''' return the node where two LL meet '''

		n1, n2 = LL_Tools.length(head1), LL_Tools.length(head2)

		# let head1 be longer LL
		if n2 > n1:
			n1, n2 = n2, n1
			head1, head2 = head2, head1
		
		# move to position where both LL have same leng remaining
		diff = n1-n2
		while diff:
			head1 = head1.next
			diff -= 1

		# now move equally in both LL and find the place of intersection
		while head1 and head2:
			if head1 == head2:
				return head1
			head1, head2 = head1.next, head2.next

	@staticmethod
	def merge_sorted_LL(head1,head2):
		''' return a sorted LL obtained from merging two sorted LL '''
		res = Node(None)
		head = res

		while head1 and head2:
			if head1.data < head2.data:
				res.next = head1
				head1 = head1.next
			else:
				res.next = head2
				head2 = head2.next
			res = res.next

		if head1:
			res.next = head1
		if head2:
			res.next = head2
		
		return head.next 

if __name__ == "__main__":

	# making a LL manually
	a = Node(10)	# head
	b = Node(20)
	c = Node(30)
	d = Node(40)
	a.next, b.next, c.next = b, c, d

	# get len of LL
	print( 'Len: ',LL_Tools.length(a) )
	
	# delete value
	print('Delete by value: ')
	a = LL_Tools.del_value(a,10)
	a = LL_Tools.del_value(a,30)
	LL_Tools.print_list(a)
	
	# insert in beginning of LL
	print('Delete by value: ') 
	a = LL_Tools.insert_beginning(a,5)
	LL_Tools.print_list(a)

	# insert at end
	print("Insert End: ")
	LL_Tools.insert_end(a,50)
	LL_Tools.print_list(a)

	# insert at kth index
	print("Insert After K:")
	a = LL_Tools.insert_after_k(a,2,100)
	a = LL_Tools.insert_after_k(a,0,200)
	LL_Tools.print_list(a)	

	# delete node in LL from front
	print('Delete at beginning: ')
	a = LL_Tools.del_beginning(a)
	LL_Tools.print_list(a)

	# delete node in LL from end
	print("Delete from end: ")
	LL_Tools.del_last(a)
	LL_Tools.print_list(a)

	# delete a node by its pointer
	print("Delete by node ref: ")
	LL_Tools.del_node(a,a.next)
	LL_Tools.print_list(a)

	# kth node from end
	print('kth node form end: ', LL_Tools.kth_node_from_end(a,2))

	# reverse the LL
	print("Reversed LL: ")
	rev = LL_Tools.reverse_LL(a)
	LL_Tools.print_list( rev )
	print("Actual LL: ")
	a = LL_Tools.reverse_LL(rev)
	LL_Tools.print_list(a)
	

	# ------------------------------------------------------------------- #

	# making a LL manually
	a = Node(10)	# head
	b = Node(20)
	c = Node(30)
	d = Node(40)
	a.next, b.next, c.next = b, c, d

	x = Node(100)
	y = Node(200)
	z = Node(300)
	x.next, y.next = y, z

	print('\nNew LL\n')
	LL_Tools.print_list(a)
	LL_Tools.print_list(x)

	# merging a LL with acother LL
	z.next = c
	LL_Tools.print_list(x)

	# get the point of merge
	n = LL_Tools.find_intersect(a,x)
	print("Intersectinf LL: ")
	LL_Tools.print_list(n)

	# ------------------------------------------------------------ #

	# making a LL manually
	a = Node(10)	# head
	b = Node(20)
	c = Node(30)
	d = Node(40)
	a.next, b.next, c.next = b, c, d

	x = Node(100)
	y = Node(200)
	z = Node(300)
	x.next, y.next = y, z
	print("Merge two sorted LL: ")
	LL_Tools.print_list( LL_Tools.merge_sorted_LL(a,x) )
