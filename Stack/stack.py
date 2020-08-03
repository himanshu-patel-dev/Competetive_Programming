class stack:
	def __init__(self):
		self.stack = []

	def pop(self):
		return self.stack.pop()

	def push(self,data):
		self.stack.append(data)

	def size(self):
		return len(self.stack)

	def peek(self):
		if len(self.stack)>0:
			return self.stack[0]
		else:
			return None
	def printStack(self):
		print(self.stack)

if __name__ == "__main__":
	s = stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.printStack()
	print(s.size())
	print(s.pop())
	print(s.peek())
	s.printStack()
