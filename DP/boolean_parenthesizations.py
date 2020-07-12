def boolean_parenthesizations(symbols, operator):
	n = len(symbols)
	T = [ [0 for i in range(n)] for j in range(n)]
	F = [ [0 for i in range(n)] for j in range(n)]

	for i in range(n):
		if symbols[i] ==  'T':
			T[i][i] = 1
			F[i][i] = 0
		else:
			T[i][i] = 0
			F[i][i] = 1
	
	for d in range(1,n):
		for i in range(n-d):
			j = i+d
			for k in range(i,j):
				# total value for true and false
				t_ik = T[i][k] + F[i][k]
				t_kj = T[k+1][j] + F[k+1][j]

				if operator[k] == '|':
					T[i][j] += t_ik*t_kj - F[i][k]*F[k+1][j]
					F[i][j] += F[i][k]*F[k+1][j]

				elif operator[k] == '&':
					T[i][j] += T[i][k]*T[k+1][j]
					F[i][j] += t_ik*t_kj - T[i][k]*T[k+1][j]
					
				elif operator[k] == '^':
					T[i][j] += ( T[i][k]*F[k+1][j] + 
									F[i][k]*T[k+1][j] 
					)
					F[i][j] += ( T[i][k]*T[k+1][j]+
									F[i][k]*F[k+1][j]
					)
	# to see matrix filled
	# for row in T:
	# 	print(row)
	# print('----------------')
	# for row in F:
	# 	print(row)
	return T[0][-1]



if __name__ == "__main__":
	# There are 4 ways  
	# ((T|T)&(F^T)), (T|(T&(F^T))),  
	# (((T|T)&F)^T) and (T|((T&F)^T))
	symbols = "TTFT"
	operator = "|&^"
	print( boolean_parenthesizations( symbols, operator )) 