def infix_to_postfix(expression):
	operator = '*+-()/'
	postfix = []
	precedence = { '+':2, '-':2, '*':3, '/':3, '(':1 }
	stack = []

	for symbol in expression:
		if symbol in operator:
			# if symbol is operator then push to stack
			if symbol is '(':
				# if opening bracket then push to stack
				stack.append(symbol)
			elif symbol is ')':
				# if closing bracket then pop till its first pair is found 
				# (exp is balanced) we are guranteed that stack is not empty
				topSym = stack.pop()
				while topSym is not '(':
					postfix.append(topSym)
					topSym = stack.pop()
			else:
				# if stack is empty or stack top is a high priority opearand
				# lower or same priority operator can't sit over another operator
				while len(stack) > 0 and precedence[ stack[-1] ] >= precedence[ symbol ]:
					postfix.append( stack.pop() )
				stack.append(symbol)
		else:
			# if symbol is operand push to result
			postfix.append(symbol)

	# empty out the stack to postfix
	while len(stack) > 0:
		postfix.append( stack.pop() )

	# list to string
	postfix = ''.join(postfix)
	return postfix

if __name__ == "__main__":
	# give input without spaces or convert 
	# string to list if spaces are there
	
	# output = ABC*+D+
	expression = "A+B*C+D"
	print( infix_to_postfix(expression) )	

	# output = AB*CD+-E-	
	expression = "A*B-(C+D)+E"
	print( infix_to_postfix(expression) )	
