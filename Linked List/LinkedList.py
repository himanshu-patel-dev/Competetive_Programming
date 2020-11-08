class Node:
	# constructor for single node
	def __init__(self):
		self.data = None
		self.next = None

class Linked_list(Node):
	def __init__(self,data):
		# initializing linked list with length and data
		self.head = Node()
		self.head.data = data

	def list_length(self):
		# gettting length of linked list
		count = 0
		current = self.head
		while current != None:
			count += 1
			current = current.next
		return count

	def insert_beginning(self,data):
		# inserting node at beginning
		newNode = Node()
		newNode.data = data
		newNode.next = self.head
		self.head = newNode
		
	def insert_end(self,data):
		# inserting node at end
		newNode = Node()
		newNode.data = data

		current = self.head
		while current.next != None:
			current = current.next
		current.next = newNode

	def insert_after_k(self,k,data):
		# insert at k th location (head is at location 0 and end at location n)
		l = self.list_length()
		if k < 0 or k > l:
			print("Not proper index")
			return None
		elif k == 0:
			self.insert_beginning(data)
		elif k == l:
			self.insert_end(data)
		else:
			newNode = Node()
			newNode.data = data
			count = 0
			current = self.head

			while count < k-1:	# zero based indexing
				count += 1
				current = current.next
			
			newNode.next = current.next
			current.next = newNode
	
	def del_beginning(self):
		if self is not None:
			self.head = self.head.next
		else:
			raise "Head is None"

	def del_last(self):
		# delete last element of list
		if self is None:
			raise "Head is None"

		previous_node = None
		current_node = self.head

		while current_node.next != None:
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = None

	def del_node(self,node):
		# deleting node by its reference passed
		if self is None:
			raise "Head is None"

		current = self.head
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
			self.head = current.next
		else:
			previous.next = current.next


	def del_value(self,value):
		# deleting node by its value (only first occurance of value)
		current = self.head
		previous = self.head

		while current.next != None and current.data != value:
			previous = current
			current = current.next

		if current.data == value:
			previous.next = current.next
		else:
			print("Value not found")

	def clear_list(self):
		# in python garbage is automatically collected
		self.head = None

	def print_list(self):
		# print entire linked list
		current = self.head
		while current.next != None:
			print(current.data,' -> ',end='')
			current = current.next
		print(current.data)

	def get_kth_node_from_end(self,k):
		# first start a pointer and move it k step forward
		# then start moving other pointers till first pointer each end
		first = self.head
		while first and k:
			first = first.next
			k -= 1

		if k:
			raise 'Less than k nodes in Linked List'

		second = self.head
		while first:
			first = first.next
			second = second.next

		return second.data

	def reverse_LL(self):
		curr, prev = self.head, None
		while curr:
			curr.next, curr, prev = prev, curr.next, curr
		return prev


if __name__ == "__main__":
	LL1 = Linked_list(10)
	LL1.insert_end(20)
	LL1.insert_end(35)
	LL1.insert_end(41)
	LL1.print_list()

	LL1.del_value(35)
	LL1.del_value(38)
	LL1.print_list()

	print(LL1.list_length())

	LL1.insert_after_k(1,15)
	LL1.print_list()

	print( LL1.get_kth_node_from_end(2) )

	print("Merge two LL")
	LL2 = Linked_list(11)
	LL2.insert_end(21)
	LL2.head.next.next = LL1.head.next.next
	LL2.print_list()


	print('Linked List Reverse')
	LL1.print_list()
	head = LL1.reverse_LL()
	while head.next:
		print(head.data,end='->')
		head = head.next
	print(head.data)

