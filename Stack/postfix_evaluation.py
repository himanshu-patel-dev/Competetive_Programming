def evaluate_postfix(postfix):
	stack = []
	operator = '*-+/'

	for symbol in postfix:
		if symbol in operator:
			# if symbol is operator then operate on two operand
			# pop two operand from stack
			a = stack.pop()
			b = stack.pop()
			# b operator a
			stack.append( eval(f"{b}{symbol}{a}") ) 
		else:
			# push the operand to stack
			stack.append(symbol)
	return stack[0]

if __name__ == "__main__":
	# exp = 2*3 - (4+5) = -3
	postfix = '23*45+-'
	print( evaluate_postfix(postfix) )

	# exp = 100/2 - 10*2 + 1 = 31
	postfix = ['100','2','/','10','2','*','-','1','+']
	print( evaluate_postfix(postfix) )
