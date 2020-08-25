class Node:
	# constructor for single node
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.stack = None

	def push(self,data):
		if self.stack is None:
			self.stack = Node(data)
		else:
			n = Node(data)
			n.next = self.stack
			self.stack = n

	def pop(self):
		if self.stack is None:
			raise "Empty Stack"
		n = self.stack
		self.stack = self.stack.next
		return n.data

	def print_stack(self):
		# print entire linked list
		current = self.stack
		while current.next != None:
			print(current.data,' -> ',end='')
			current = current.next
		print(current.data)


if __name__ == "__main__":
	s = Stack()
	s.push(10)
	s.push(20)
	s.push(30)
	s.print_stack()
	print("Pop: ",s.pop())
	s.print_stack()