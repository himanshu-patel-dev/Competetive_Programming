class Node:
	# constructor for single node
	def __init__(self):
		self.data = None
		self.next = None

	# method to work on node data
	def set_data(self,data):
		self.data = data

	def get_data(self):
		return self.data 

	def set_next(self,next):
		self.next = next

	def get_next(self):
		return self.next

	def has_next(self):
		return self.next != None


class Linked_list(Node):
	def __init__(self,data):
		# initializing linked list with length and data
		self.head = Node()
		self.head.data = data
		self.length = 1

	def list_length(self):
		# gettting length of linked list
		count = 0
		current = self.head
		while current != None:
			count += 1
			current = current.get_next()
		return count

	def insert_beginning(self,data):
		# inserting node at beginning
		newNode = Node()
		newNode.set_data(data)
		newNode.set_next(self.head)
		self.head = newNode
		self.length += 1
		
	def insert_end(self,data):
		# inserting node at end
		newNode = Node()
		newNode.set_data(data)

		current = self.head
		while current.get_next() != None:
			current = current.get_next()
		
		current.set_next(newNode)
		self.length += 1

	def insert_after_k(self,k,data):
		# insert at k th location (head is at location 0 and end at location n)
		if k < 0 or k > self.length:
			print("Not proper index")
			return None
		elif k == 0:
			self.insert_beginning(data)
		elif k == self.length:
			self.insert_end(data)
		else:
			newNode = Node()
			newNode.set_data(data)
			count = 0
			current = self.head

			while count < k-1:	# zero based indexing
				count += 1
				current = current.get_next()
			
			newNode.set_next( current.get_next() )
			current.set_next( newNode )
			self.length += 1
	
	def del_beginning(self):
		# delete beginning list
		if self.length == 0:
			print("list is empty")
		else:
			self.head = self.head.get_next()
			self.length -= 1

	def del_last(self):
		# delete last element of list
		if self.length == 0:
			print("List is empty")
		else:
			previous_node = None
			current_node = self.head

			while current_node.get_next() != None:
				previous_node = current_node
				current_node = current_node.get_next()

			previous_node.set_next(None)
			self.length -= 1

	def del_node(self,node):
		# deleting node by its reference passed
		if self.length == 0:
			raise ValueError("List is empty")
		else:
			current = self.head
			previous = None
			found = False

			while not found:
				if current == Node:
					found = True
				elif current is None:
					raise ValueError("Node not found")
				else:
					previous = current
					current = current.get_next()
			
			if previous is None:
				self.head = current.get_next()
			else:
				previous.set_next(current.get_next())

			self.length -= 1
	
	def del_value(self,value):
		# deleting node by its value (only first occurance of value)
		current = self.head
		previous = self.head

		while current.get_next() != None and current.data != value:
			previous = current
			current = current.get_next()

		if current.data == value:
			previous.set_next( current.get_next() )
		else:
			print("Value not found")

	def clear_list(self):
		# in python garbage is automatically collected
		self.head = None

	def print_list(self):
		# print entire linked list
		current = self.head
		while current.get_next() != None:
			print(current.get_data(),' -> ',end='')
			current = current.get_next()
		print(current.get_data())


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
