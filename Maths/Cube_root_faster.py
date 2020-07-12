# find cubic root of a number using Binary Search 

def diff(n, mid) : 
	"""	time comp = O(log(n)) """
	# it shows how much we differ in actual and current root 'mid'
	# if difference is acceptable we accept mid as root
	return abs(n - (mid * mid * mid)) 

def cubicRoot(n) : 
	# Set start and end for binary search 
	start = 0
	end = n 
	
	# Set precision for acceptance
	e = 0.0000001
	while (True) : 
			
		mid = (start + end) / 2
		error = diff(n, mid) 

		# If error is less than e then accept mid as answer
		if (error <= e) : 
			return mid 
			
		if ((mid * mid * mid) > n) : 
			end = mid 
		else : 
			start = mid 
if __name__ == "__main__":
	# n = 125
	n = 64
	print( cubicRoot(n) )
