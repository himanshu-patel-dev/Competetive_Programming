def Push(x,stack1,stack2):
	stack1.append(x)

def Pop(stack1,stack2):
	# if stack 2 is empty then pop out stack 1 into it
	if not stack2:
		while stack1:
			stack2.append( stack1.pop() )

	# if still stack2 is empty then -1 else pop out element
	if stack2:
		return stack2.pop()
	else:
		return -1

if __name__ == "__main__":
	st1 = []
	st2 = []
	lst = [1,2,3]

	for ele in lst:
		Push(ele,st1,st2)
	print( st1, st2 )
	# pop sequence same as queue
	for i in range(2):
		print( Pop(st1,st2) )
