def optimal_jump_to_reach_last_element(lst):
	"""
	return the min no of jumps required to reach the last position 
	starting from first, each jump can be less than or equal to value
	at position lst[i]
	"""
	n = len(lst)
	dp = [float('inf') for i in range(n)]
	dp[0] = 0
	jump_index = [-1]*n

	# iterating  from 1 to n-1
	for i in range(1,n):
		# for each iteration we can go from j = (0 to i-1) 
		# and check for pos j form which we can reach i in lesser jumps
		for j in range(i):
			# checking if we can reach i from this index of j
			if j + lst[j] >= i and dp[j] != float('inf'):
				# also if this num of jump is lesser than earlier value of i
				if dp[j]+1 < dp[i]:
					dp[i] = dp[j]+1	
					jump_index[i] = j	# stores the index from where we made jump to i 
				break
	# print(dp)
	# print(jump_index)

	# getting sequence of jumps
	index = n-1		# we currently at index n-1 (last), 
	# with help of junp_index we try to get index from which we reached current index
	jump_seq = [index]
	while index != 0:
		index = jump_index[index]
		jump_seq.append(index)

	# min no of jumps required and its jump sequence
	return (dp[n-1], jump_seq[::-1])

if __name__ == "__main__":
	# lst = [1, 3, 6, 1, 0, 9]
	lst = [2,3,1,1,2,4,2,0,1,1]
	print( optimal_jump_to_reach_last_element(lst) )