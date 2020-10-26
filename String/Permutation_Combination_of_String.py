from itertools import permutations, combinations
def permutation_inbuilt(string):
	return [ ''.join(perm) for perm in permutations(string) ]

def combination_inbuilt(string,n):
	return [ ''.join(comb) for comb in combinations(string,n) ]

def permutaion_func(string):
	# if string is empty
	if len(string) == 0:
		return []

	# if empty is one char
	if len(string) == 1:
		return [string]

	result = []
	# more than one char
	for i in range(len(string)):
		# get the i th char
		m = string[i]
		# remaining list
		remList = string[:i] + string[i+1:]
		for perm in permutaion_func(remList):
			result.append( [m] + perm )
	return result

if __name__ == "__main__":
	string = "abc"
	print( permutation_inbuilt(string) )

	string = list("abc")
	lst = permutaion_func(string)
	print( [ ''.join(perm) for perm in lst ] )

	string = "abc"
	print( combination_inbuilt(string,2) )
