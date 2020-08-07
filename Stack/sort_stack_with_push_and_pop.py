""" sort stack with only push and pop  """
""" time comp = O(n*n) """

def sorted_insert(stack,element):
	if not stack or stack[-1] < element:
		stack.append(element)
	else:
		temp = stack.pop()
		sorted_insert(stack,element)
		stack.append(temp)

def sort_stack(stack):
	if stack:
		temp = stack.pop()
		sort_stack(stack)
		sorted_insert(stack,temp)

if __name__ == "__main__":
	stack = [2,4,1,7,6,3]
	sort_stack(stack)
	print( stack )
