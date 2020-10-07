def match_bruteforce(t,p):
	""" 
	Match pattern in text
	n = len(text) m = len(pattern)
	T = O( (n-m+1)*m ) 	
	for each char in pattern we have to 
	search for m char of pattern
	S = O(1)
	"""
	n,m = len(t), len(p)
	for i in range(n-m+1):
		stri, pati = i,0	# take seperate index to compare both
		while stri < n and pati < m and t[stri] == p[pati]:
			stri += 1
			pati += 1
		if pati == m:
			# return the index of first char and next to last char 
			# in text if found a match
			return (stri-m,stri)
	# return -1 if a match not found
	return None

def Robin_Carp_Match(t,p):
	"""
	T = O(n-m+1)
	S = O(m)
	"""
	if not p or not t:
		return None

	n,m = len(t), len(p)
	pattern_hash = set(p)

	for i in range(n-m+1):
		text_hash = set(t[i:i+m])
		# if both hash do not combine than 
		if text_hash != pattern_hash:
			continue
		
		stri, pati = i, 0
		while stri<n and pati<m and t[stri] == p[pati]:
			stri += 1
			pati += 1
		if pati == m:
			return (stri-m,stri)

	return None

def Prefix_Table(p):
	# T = O(n)
	# make a prefix table for pattern
	n = len(p)
	F = [0]*n

	k = 0
	for i in range(1,n):
		# if k > 0 it means some of the pattern has already matched 
		# with text till now 
		while k > 0 and p[k] != p[i]:
			k = F[k-1]

		# inc k if pattern at index k 
		if p[k] == p[i]:
			k += 1
		# k rep a size of suffix which is same as prefix
		F[i] = k
	return F

def KMP(t,p):
	# T = O(n+m)
	n,m = len(t), len(p)
	F = Prefix_Table(p)

	q = 0
	for i in range(1,n):
		# q>0 means currently we had a match of len > 0 in bw text and pattern
		if q > 0 and t[i] != p[q]:
			q = F[q-1]

		# inc q if current char of pattern match with char at index q of text
		if t[i] == p[q]:
			q += 1
		
		# len of pattern in t that matchs with p has become m then its a match
		if q == m:
			return (i-m+1,i+1)
	return None
		

if __name__ == "__main__":
	p = "hello"									# pattern
	t = "This is basic hello world program"		# text 
	
	# brute force
	found = match_bruteforce(t,p)
	if found:
		print(t[found[0]:found[1]])
	else:
		print("Not found by brute force")

	# robin karp
	found = Robin_Carp_Match(t,p)
	if found:
		print(t[found[0]:found[1]])
	else:
		print("Not found by robin karp")

	p = "ababaca"									# pattern
	t = "bacbabababacaca"		# text 
	# KMP
	found = KMP(t,p)
	if found:
		print(t[found[0]:found[1]])
	else:
		print("Not found by KMP")
