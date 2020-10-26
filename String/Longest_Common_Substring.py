def LCS(string1, string2):
	"""
	Longest Common Substring between two string s1 and s2
	T = O( n*m )
	S = O( n*m )
	"""
	n1, n2 = len(string1), len(string2)

	dp = [ [0 for j in range(n2+1)] for i in range(n1+1) ]

	max_len = 0				# to store the max value of dp cells
	max_len_ij = (0,0)		# to store the index of max dp cell 

	for i in range(1,n1+1):
		for j in range(1,n2+1):
			# if both the string have equal char then
			# dp get an update based on diagonally previous value
			if string1[i-1] == string2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1

				if dp[i][j] > max_len:
					max_len = dp[i][j]
					max_len_ij = (i,j)

	# from the index of max value in dp get the 
	# sub string which is longest between two
	i,j = max_len_ij
	sub_str = []
	while i>0 and j>0 and dp[i][j] > 0:
		sub_str.append( string2[j-1] )
		i -= 1
		j -= 1

	res = ''.join(sub_str[::-1])
	return ( res, max_len )


if __name__ == "__main__":
	
	string1 = "HelloWorld"
	string2 = "xxxxWorld"
	print( LCS(string1,string2) )

	string1 = "HelloWorld"
	string2 = ""
	print( LCS(string1,string2) )

	string1 = "HelloWorld"
	string2 = "xxxxxxxxxx"
	print( LCS(string1,string2) )

	string1 = ""
	string2 = "xxxxWorld"
	print( LCS(string1,string2) )

	string1 = "abcdef"
	string2 = "xabcx"
	print( LCS(string1,string2) )
