def Remove_Interval(intervals):
	# idea: a long interval starts early and finishes late thus we want to
	# select as many short interval as possible and remove only larger ones
	# for this we sort interval based on their ending location 

	# we move in a greedy way and select interval which end as early as poss
	# and discard next overlapping interval

	# sort intervals based on second index 
	intervals.sort(key = lambda x: x[1])
	curr_interval = intervals[0]
	res = []

	for interval in intervals[1:]:
		if interval[0] >= curr_interval[1]:
			res.append(curr_interval)
			curr_interval = interval
	res.append(curr_interval)

	return res	

def Remove_Interval(intervals):
	# we move in a greedy way and select interval which end as early as poss
	# and discard next overlapping interval which conflict with previously
	# selected interval

	# sort intervals based on second index 
	intervals.sort(key = lambda x: x[1])
	last_end = -1
	res = []

	for i,interval in enumerate(intervals):
		# if next interval do not conflict with prev interval select it
		# and update the end time
		if interval[0] > last_end:
			res.append(i)
			last_end = interval[1]

	# return the selected intervals
	return [ intervals[i] for i in res ]

if __name__ == "__main__":
	lst = [
		[ 19, 25 ], 
		[ 10, 20 ], 
		[ 16, 20 ]
	]
	print( Remove_Interval(lst) )


	lst = [
		[ 1, 2 ], 
		[ 4, 7 ], 
		[ 3, 8 ]
	]
	print( Remove_Interval(lst) )

	lst = [
		[ 1, 2 ], 
		[ 5, 10 ], 
		[ 18, 35 ],
		[ 40, 45]
	]
	print( Remove_Interval(lst) )
