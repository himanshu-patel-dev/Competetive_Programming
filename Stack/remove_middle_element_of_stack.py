""" remove middle element of stack without using any other data structure and O(n) time """

def reach_middle(stack,size,counter):
	""" size is stack size and counter is count of element poped """
	if size//2 == counter:
		stack.pop()
	else:
		t = stack.pop()
		reach_middle(stack,size,counter+1)
		stack.append(t)

def deleteMid(stack):
	""" s is stack """
	reach_middle(stack,len(stack),0)
	return stack

if __name__ == "__main__":
	stack = [1,2,3,4,5]
	print( deleteMid(stack) )

	stack = [1,2,3,4]
	print( deleteMid(stack) )
