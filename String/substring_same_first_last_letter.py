from collections import defaultdict
def substring_same_first_last_letter(string):
	"""
	return no of substring in which first and last character are same
	"""
	d = defaultdict(int)
	for e in string:
		d[e] += 1
	
	c = 0
	for e,v in d.items():
		if v > 1:
			c += v*(v-1)//2
	return c + len(string)

if __name__ == "__main__":
		s = "abcab"	# a, abca, b, bcab, c, a and b 
		# ans = 7
		print( substring_same_first_last_letter(s) )