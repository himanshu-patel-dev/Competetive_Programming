def check_balanced_paranthesis(sequence):
	stack = []
	pairs = {
		'(': ')',
		'[': ']',
		'{': '}',
		'}': '{',
		')': '(',
		']': '['
	}
	opening = '([{'

	n = len(sequence)
	for p in sequence:
		# opening parenthesis
		if p in pairs:
			if p in opening:
				stack.append(p)
			elif pairs[p] == stack[-1]:
				stack.pop()
	return len(stack) == 0

if __name__ == "__main__":
	print( check_balanced_paranthesis('({[()]})') )
	print( check_balanced_paranthesis('([a+b]*{c-d})') )
	print( check_balanced_paranthesis('[(]') )
	
	