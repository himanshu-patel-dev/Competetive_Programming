def  Zero_One_knapsack(capacity, index, weight, value):
	if index < 0 or capacity < min(weight):
		return 0
	else:
		if capacity >= weight[index]:
			a = Zero_One_knapsack(capacity, index-1, weight, value)
			b = Zero_One_knapsack(capacity - weight[index], index-1, weight, value) + value[index]
			return max( a,b )
		else:
			return Zero_One_knapsack(capacity, index-1, weight, value)

if __name__ == "__main__":
	value = [ 60, 100, 120 ]
	weight = [10, 20, 30]
	index = len(value)-1
	capacity = 25
	print( Zero_One_knapsack(capacity, index, weight, value) )
