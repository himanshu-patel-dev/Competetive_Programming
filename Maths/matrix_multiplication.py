def Matrix_multiplication(lst1, lst2):
	if len(lst1[0]) != len(lst2):
		return "Incorrect Dimensions"
	else:
		row = len(lst1)
		col = len(lst2[0])
		result = [ [0 for i in range(col)] for j in range(row)]
		
		for i in range(row):
			for j in range(col):
				for k in range( len(lst1[0]) ):
					result[i][j] += lst1[i][k] * lst2[k][j]
		return result
