def remove_repeated_char(string):
	stack = []
	for char in string:
		# if stack is empty push into the stack and continue
		if not stack or stack[-1] != char:
			stack.append( char )
		else:
			stack.pop()
	string = ''.join(stack)
	return string

if __name__ == "__main__":
	# string = "mississippi"
	print( remove_repeated_char(string) )