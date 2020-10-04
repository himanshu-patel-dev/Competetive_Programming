from collections import Counter, defaultdict

def pattern_in_string_window(s,p):
	n1,n2 = len(p), len(s)
	
	# dict to count occurance of all char in pattern and string
	p_count = Counter(p)
	s_count = defaultdict(int)	
	start = 0		# pointer to start of window
	count = 0		# count of no of pattern char found in curr window
	window_start = -1 # this holds final start pos of window which is min in len
	len_window = float('inf')

	for end in range(n2):
		c = s[end]		# current char

		# inc count only when a char is found which is required to complete 
		# pattern in current window
		if c in p_count and p_count[c] > s_count[c]:
			count += 1
		# inc count of char in s
		s_count[c] += 1


		# if all char of pattern are found in window
		if count == n1:
			# pick the starting ele of sliding window
			e = s[start]
			# if e is not in pattern or its count its more than what is required
			# then we must remove this ele from window by inc the start 
			while e not in p_count or s_count[e] > p_count[e]:
				if s_count[e] > p_count[e]:
					s_count[e] -= 1
				start += 1		# dec the size of window
				e = s[start]
			# start is start index of win and end is end index of window
			# if found a samller len window then update the len and start pos
			# of window
			if len_window > end - start + 1:
				len_window = end-start+1
				window_start = start
	
	window_end = window_start + len_window

	if window_start == -1:
		print("No such window found")
		return
	
	return s[window_start:window_end]


if __name__ == "__main__":
	s = "this is a test string"	# string
	p = "tist"					# pattern
	print( pattern_in_string_window(s,p) )


	s = "go for gold"	# string
	p = "ofo"			# pattern
	print( pattern_in_string_window(s,p) )