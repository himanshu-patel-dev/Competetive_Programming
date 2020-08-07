def flip(string):    
	stack = []
	for b in string:
		# if its a { then push to stack
		if b == '{':
			stack.append('{')
		else:
			# if its a } then ckeck for its matching pair on
			# top of stack if founf pop else push } on stack
			if stack and stack[-1] == '{':
				stack.pop()
			else:
				stack.append('}')

	# when this finish in stack we have all those brackets left
	# which do not get a mathchin pair all pairs in bwt get vanished
	# print( stack )


	n = len(stack)
	# if leg is even we can form balance else not
	if n%2 == 0:
		right = stack.count('}')
		left = stack.count('{')
		# if there are n { then to balance then 
		# we flip any n//2 { bracket if n is even
		# else if n is odd then we flip n//2 {
		# if { in odd then } also in odd thus m//2 for }
		# and +2 for 1 pair { and }
		result = right//2 + left//2
		if left%2 != 0:
			result += 2
		return result
	else:
		return -1

if __name__ == "__main__":
	
	string = '}{}{}{}}}{{{{{}{}{}}{{}{}{}}{{}}{{'
	print( flip(string) )

	string = '{{}{}}}{'
	print( flip(string) )