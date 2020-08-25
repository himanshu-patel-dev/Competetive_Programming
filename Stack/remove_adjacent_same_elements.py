def remove_adjacent(lst):
	"""
	if as element have its consecutive element same as 
	itself then remove all such elements
	"""
	stack = []
	n = len(lst)

	for i in range(n):
		add = True
		while stack and stack[-1] == lst[i]:
			stack.pop()
			add = False
		if add:
			stack.append(lst[i])
	return stack

if __name__ == "__main__":
	lst = 'tom jerry jerry tom'.split()
	print( remove_adjacent(lst) )

	lst = "ab aa aa bcd ab".split()
	print( remove_adjacent(lst) )
