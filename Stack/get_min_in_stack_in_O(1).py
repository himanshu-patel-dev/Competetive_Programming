class Min_stack:
	""" 
	stack with modified push and pop operations 
	so as to get min of stack in O(1) time 
	"""

	def __init__(self):
		self.main_stack = []
		self.min_stack = []

	def push(self,data):
		if len(self.main_stack) == 0:
			self.main_stack.append( data )
			self.min_stack.append( data )
		else:
			m = min(self.min_stack[-1],data)
			self.main_stack.append(data)
			self.min_stack.append(m)
		

	def pop(self):
		if len(self.main_stack) == 0:
			raise "Stack Empty"

		self.min_stack.pop()		# remove min value
		self.main_stack.pop()		# remove top most element

	def min_in_stack(self):
		# return min in current stack without poping element
		return self.min_stack[-1]

if __name__ == "__main__":
	lst = [2,6,4,1,5]
	s = Min_stack()

	for ele in lst:
		s.push(ele)

	print( s.main_stack, s.min_stack )

