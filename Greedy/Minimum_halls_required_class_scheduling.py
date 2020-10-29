"""
Minimum no of room required to schedule all classes on time
T = O(n)
S = O(1)
"""

def minHalls(timing):
	MAX_LEN = 100
	prefix_sum = [0]*MAX_LEN

	for start,end in timing:
		# add one more class to schedule
		prefix_sum[start] += 1
		# specify closing of this class
		prefix_sum[end+1] -= 1

	for i in range(1,MAX_LEN):
		prefix_sum[i] += prefix_sum[i-1]

	return max(prefix_sum)


if __name__ == "__main__":
	class_timing = [ 
		[0,5],
		[1,2],
		[1,10],
	]
	print(  minHalls(class_timing) )