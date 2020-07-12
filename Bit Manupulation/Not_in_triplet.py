def Not_in_triplet(lst):
	"""
	all numbers in lst are in triplets except one (which occur only one time) identify which one
	"""
	one = two = 0
	for ele in lst:
		# select bits which already had odd occurance but now occured in ele also so two occurance total
		two = two | ( one & ele )	
		# select bits which had odd occurance
		one = one ^ ele

		# bits which occured in both have three occurance remove those bits
		bit_mask = ~(one & two)	# ~ is taking ones complement
		one = one & bit_mask
		two = two & bit_mask

	return one

if __name__ == "__main__":
	lst = [1,1,1,2,2,2,4]
	print( Not_in_triplet(lst) )