def delete_next_greater_element(lst,k):
	n = len(lst)
	stack = []

	for i in range(n):	
		while k and stack and stack[-1] < lst[i]:
			stack.pop()
			k -= 1
		stack.append(lst[i])

	return stack

if __name__ == "__main__":
	lst = [20,10,25,30,45]
	k = 2
	print( delete_next_greater_element(lst,k) )