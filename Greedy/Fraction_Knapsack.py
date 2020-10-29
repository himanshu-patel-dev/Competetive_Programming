def Fractionl_KS(weight, cost, capacity):
	fraction_gain = [ round(cost[i]/weight[i],4) for i in range(len(weight))]

	# zip all list element wise into pairs
	zipped_pairs = zip(weight,cost,fraction_gain)
	# sort based on fraction gain
	zipped_pairs = sorted(zipped_pairs,key = lambda x: x[2], reverse=True)	
	# zip all pairs back list wise
	zipped_list = zip(*zipped_pairs)
	# assign list to each back to each name
	weight, cost, fraction_gain = [ list(tup) for tup in zipped_list]
	
	# print(cost)
	# print(weight)
	# print(fraction_gain)

	Total = 0
	for i, w in enumerate(weight):
		if w <= capacity:
			Total += cost[i]
			capacity -= w
		else:
			Total += fraction_gain[i]*capacity
			break
	return Total

if __name__ == "__main__":
	weight = [10, 40, 20, 30]
	cost = [60, 40, 100, 120]
	capacity = 50

	print( Fractionl_KS(weight, cost, capacity) )
