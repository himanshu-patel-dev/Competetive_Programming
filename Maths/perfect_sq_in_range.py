import math
def perfect_sq_in_range(a,b):
	a_sqrt = math.ceil( math.sqrt(a) )
	b_sqrt = math.floor( math.sqrt(b) )
	return b_sqrt - a_sqrt + 1

if __name__ == "__main__":
	a,b = 1,10 # ans = 3 as 1 4 9
	print( perfect_sq_in_range(a,b) )