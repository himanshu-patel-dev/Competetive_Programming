from  math import log2

def log(val):
	if not val:
		return 0
	return log2(val)

def entropy(final_col):
	s = sum(final_col)
	res = 0
	for val in final_col:
		res += -(val/s)*log(val/s)
	return round(res,3)

def func(a,b,c,d):
	return a*( -(c/a)*(log(c/a)) - (d/a)*log(d/a) )/b

def func2(matrix):
	return sum([ func(row[0],row[1], row[2], row[3]) for row in matrix])

def func3(matrices):
	return [ round(func2(matrix),3) for matrix in matrices]

if __name__ == "__main__":
	col2 = [

		# value 2 count, 
		# Total count in attribute, 
		# Yes out of value2, 
		# No out of value 2 
		[2,5,2,0],		# value 1
		[2,5,1,1],		# value 2
		[1,5,1,0]		# value 3
	]

	col3 = [

		# value 3 count, 
		# Total count in attribute, 
		# Yes out of value3, 
		# No out of value 3	 
		[2,5,2,0],		# value 1
		[3,5,0,3],		# value 2
	]

	col4 = [

		# value 4 count, 
		# Total count in attribute, 
		# Yes out of value4, 
		# No out of value 4 
		[3,5,1,2],		# value 1
		[2,5,1,1],		# value 2
	]

	matrices = [col2,col3,col4]

	# count of various unique values in result column 
	final_col = [3,2]
	ent = entropy(final_col)

	result = func3(matrices)

	print("Total Entropy: ",ent)
	print("Entropy of all columns: ",result)
	print("Min Entropy: ",min(result))
	print( "Max Gain: ",ent-min(result))