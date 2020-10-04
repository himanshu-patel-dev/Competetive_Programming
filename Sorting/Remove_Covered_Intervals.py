"""
Given a list of intervals, remove all intervals that are covered 
by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.
"""

class Solution:
	""" T = O(n) and S = O(n) """
	# slow
	def removeCoveredIntervals(self, intervals):
		if not intervals:
			return 0

		n = len(intervals)
		intervals.sort()
			
		res = [ intervals[0] ]
		for i in range(1,n):
			prev = res[-1]
			curr = intervals[i]
			
			# if current is covered by prev skip current tuple
			if prev[0] <= curr[0] and curr[1] <= prev[1]:
				continue
			
			# if prev is covered by current interval pop prev and insert current
			while res and curr[0] <= prev[0] and prev[1] <= curr[1]:
				res.pop()
			res.append(curr)

		return len(res)
					
class Solution:
	""" T = O(n) and S = O(1) """
	# fast
	def removeCoveredIntervals(self, intervals):
		if not intervals:
			return 0

		ans = len(intervals)
		# if two interval have same start place the one 
		# with higher end in front
		intervals.sort(key = lambda x: (x[0],-x[1]))
			
		# placeholder for left and right limit reached
		left,right = intervals[0]
			
		# left will always be less than or equal to start
		for start,end in intervals[1:]:
			# if end is less than right means this interval 
			# is already covered
			if end <= right:
				ans -= 1
			# if start is over right then then reset limits to catch 
			# upcoming overlap intervals
			elif start > right:
				left, right = start, end
			# start is in between left and right but end is beyond 
			# right then extend right
			else:
				right = end
				
		return ans


if __name__ == "__main__":
	s = Solution()

	lst = [[1,2],[1,4],[3,4]]
	print( s.removeCoveredIntervals(lst) )

	lst = [[3,10],[4,10],[5,11]]
	print( s.removeCoveredIntervals(lst) )

	lst = [[0,10],[5,12]]
	print( s.removeCoveredIntervals(lst) )

	lst = [[1,4],[2,3]]
	print( s.removeCoveredIntervals(lst) )

	lst = [[1,4],[3,6],[2,8]]
	print( s.removeCoveredIntervals(lst) )
