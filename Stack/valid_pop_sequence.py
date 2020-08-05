def valid_pop_sequence(push,pop):
	stack = []
	elements_poped = 0
	total = len(pop)

	for ele in push:
		stack.append(ele)

		while elements_poped < total and stack and stack[-1] == pop[elements_poped]: 
			stack.pop()
			elements_poped += 1

	return elements_poped == total

if __name__ == "__main__":
	push_sequence = [1,2,3,4,5,6]
	pop_sequence = [4,5,3,2,1,6]
	print( valid_pop_sequence(push_sequence, pop_sequence) )

	push_sequence = [1,2,3,4,5,6]
	pop_sequence = [1,5,4,6,2,3]
	print( valid_pop_sequence(push_sequence, pop_sequence) )

	push_sequence = [4,5,6]
	pop_sequence = [6,5,4]
	print( valid_pop_sequence(push_sequence, pop_sequence) )
