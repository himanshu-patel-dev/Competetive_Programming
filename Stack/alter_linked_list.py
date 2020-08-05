class Node:
	# constructor for single node
	def __init__(self,data):
		self.data = data
		self.next = None

	def print_list(self):
		# print entire linked list
		while self.next != None:
			print(self.data,' -> ',end='')
			self = self.next
		print(self.data)

def alter_linked_list(head):
	if head is None:
		return head
	
	# fill the stack with linked list
	stack = []
	temp = head
	while temp:
		stack.append( temp )
		temp = temp.next

	iterator = head			# starting from head 
	stack_turn = True		# first element is added now its turn of stack
	head_front = head

	# this condition imply that what ever we are going to add to 
	# iterator either form stack or from Linked List is not already 
	# present in iterator, if it is then break
	while (stack_turn and iterator != stack[-1]) or	(not stack_turn and iterator != head_front):
		if stack_turn:
			head_front = head_front.next
			# this must be done before assigning the iterator.next to poped element 
			# becuse after the assignment current linked list itself is changed and
			# at this time head_front and iterator are pointing to same element in LL 
			iterator.next = stack.pop()
		else:
			iterator.next = head_front
		# flip turn and increment iterator
		stack_turn = not stack_turn
		iterator = iterator.next
	# do apply this so that to end loop in linked list
	iterator.next = None

	return head

if __name__ == "__main__":
	LL1 = Node(10)
	LL1.next = Node(20)
	LL1.next.next = Node(30)
	LL1.next.next.next = Node(40)
	LL1.next.next.next.next = Node(50)

	print("Initial LL: ",end='')
	LL1.print_list()

	LL1 = alter_linked_list(LL1)

	print("Final LL: ",end='')
	LL1.print_list()
	