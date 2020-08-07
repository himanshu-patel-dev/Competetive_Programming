def bracket_sequence(string):
	""" print the seqence in which new bracket get open and earlier bracket get closed  """
	stack = []
	result = []
	counter = 1
	n = len(string)
	for i in range(n):
		if string[i] == '(':
			stack.append(counter)			# add sequence of opening braket to stack
			result.append(counter)
			counter += 1					# count opening of new bracket
		elif string[i] == ')':
			result.append( stack.pop() )	# pop stack and get sequence of last opened bracket
			
	result = ' '.join(map(str, result))

if __name__ == "__main__":
	# (a+(b*c))+(d/e)​
	# 1 2 2 1 3 3
	print( bracket_sequence(string) )

	# ((())(()))
	# 1 2 3 3 2 4 5 5 4 1
	print( bracket_sequence(string) )

	# ((((()
	# 1 2 3 4 5 5
	print( bracket_sequence(string) )	
