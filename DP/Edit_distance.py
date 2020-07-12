def  Edit_Distance(str1, str2):
	"""
	cod = cost of deletion = 1
	cor = cost of replacement = 0 or 1 (cost)
	coi = cost of insertion = 1
	"""
	coi = 1
	cod = 1
	cor = 1

	row = len(str1)
	col = len(str2)

	dp = [ [0 for j in range(col+1)] for i in range(row+1)]

	for i in range(row+1):
		for j in range(col+1):

			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			else:
				cost = 0 if str1[i-1] == str2[j-1] else cor
				dp[i][j] = min(
					dp[i-1][j] + cod,
					dp[i][j-1] + coi,
					dp[i-1][j-1] + cost
				)
	# for r in dp:
	# 	print(r)
	return dp[-1][-1]

if __name__ == "__main__":
	str1 = "nituttarakhand"
	str2 = "mnitjaipur"
	# ans = 3
	print( Edit_Distance(str1,str2) )
