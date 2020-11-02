def max_stock(lst,k):
	""" 
	by making at most k transaction get the max profit from given 
	list (containing stock prize of each day) you can't buy before 
	selling previous stock. At a time you can hold only one stock.
	But you may sell and buy at same day
		T = O(k*n)
		S = O(k*n)

		Refer: Tushar Roy DP
	"""
	if len(lst) < 2:
		return 0

	row = k+1
	col = len(lst)
	dp = [ [0]*col for i in range(row)]

	for i in range(1,row):
		# first col of DP is 0 so max diff initially is -lst[0]
		# and we start from col 1
		maxDiff = - lst[0]	
		for j in range(1,col):
			# consider term dp[i][j-1] is like we are happy with profit 
			# of day j-1 and max obtained till j-1 is more than today 
			dp[i][j] = max(dp[i][j-1], lst[j] + maxDiff )
			# update maxDiff
			maxDiff = max(maxDiff, dp[i-1][j] - lst[j])
	
	# for r in dp:
	# 	print(r)

	return dp[row-1][col-1]		

def max_stock_two_transaction(lst):
	"""
	same as above but at most 2 transaction are allowed
	"""
	n = len(lst)
	if n < 2:
		return 0
	
	profit1 = [0]*n
	profit2 = [0]*n
	min_by_now = lst[0]
	max_by_now = lst[n-1]
	
	for i in range(1,n):
		# getting tha max profit we can get selling 
		# at index i starting from index 0 
		profit1[i] = max(profit1[i-1], lst[i] - min_by_now)
		# update the min we got till i indexes
		min_by_now = min(min_by_now, prices[i])
		
		j = n-1-i
		# getting tha max profit we can get selling 
		# at index j starting from index n-1
		profit2[j] = max(profit2[j+1], max_by_now - lst[j] )
		# update the max we got till j indexes
		max_by_now = max(max_by_now, prices[j])

	# find the index where the two values are max it is 
	# the place where we should sell first stock and buy another
	result = 0
	for i in range(n):
		result = max(result, profit1[i]+profit2[i])
	return result

if __name__ == "__main__":
	stocks = [3,3,5,0,0,3,1,4]
	print( max_stock(stocks,2) )

	stocks = [1,2,3,4,5]
	print( max_stock(stocks,2) )

	stocks = [7,6,4,3,1]
	print( max_stock(stocks,2) )


