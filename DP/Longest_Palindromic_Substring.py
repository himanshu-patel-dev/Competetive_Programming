def Longest_Palindromic_Substring(string):
	""" return string of largest length which is palindrome """
	n = len(string)
	dp = [ [False for i in range(n)] for j in range(n) ]

	# initialize first diagonal
	for i in range(n):
		dp[i][i] = True
	# initialize second diagonal
	for i in range(n-1):
		if string[i] == string[i+1]:
			dp[i][i+1] = True

	# rest of the diagonal
	a,b = 0,0 	#coordiante to record max len palindrome string 
	for k in range(2,n):
		for i in range(n-k):
			j = i + k

			if dp[i+1][j-1] & (string[i] == string[j]):
				dp[i][j] = True
				# if len of new segment is greater than len of previous seg
				if (j-i+1) > (b-a+1):	
					a,b = i,j

	# for row in dp:
	# 	print(row)
	return string[a:b+1]

if __name__ == "__main__":
	string = "GEEKEG"
	print( Longest_Palindromic_Substring(string) )
