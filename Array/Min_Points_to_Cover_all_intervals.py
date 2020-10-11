"""
Minimum Number of Arrows to Burst Balloons

There are some spherical balloons spread in two-dimensional space. 
For each balloon, provided input is the start and end coordinates of 
the horizontal diameter. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points 
along the x-axis. A balloon with x_start and x_end bursts by an arrow 
shot at x if x_start ≤ x ≤ x_end. An arrow once shot keeps traveling 
up infinitely.

Given an array points where points[i] = [xstart, xend], return the 
minimum number of arrows that must be shot to burst all balloons.
"""

class Solution:
	def findMinArrowShots(self, points):
		if not points:
			return 0

		# sorting all intervals
		points.sort()
		arrows = []

		for start,end in points:
			# print(arrows, (start,end))
			if not arrows:
				arrows.append( (start,end) )
				continue
			
			# if there are tuples in list arrows fetch the last one
			# since the intervals are sorted the new coming tuple can 
			# only overlap with last arrow interval no need to check all 
			# interval in arrow list
			last = arrows[-1]

			# prev interval do not overlap with current
			if last[1] < start:
				arrows.append( (start,end) )	# puch new interval
			else:
				new = ( max(start,last[0]) , min(end,last[1]) )
				arrows.pop()
				arrows.append( new )

		return len(arrows)

# Faster
class Solution:
    def findMinArrowShots(self, A):
        if not A: return 0
        A.sort(key=lambda x:x[1])
        ret = 1
        right = A[0][1]
        for x,y in A:
            if x<=right:
                continue
            ret += 1
            right = y
        return ret

if __name__ == "__main__":
	s = Solution()

	points = [[10,16],[2,8],[1,6],[7,12]]
	# print( s.findMinArrowShots(points) )

	points = [[1,2],[3,4],[5,6],[7,8]]
	# print( s.findMinArrowShots(points) )

	points = [[1,2],[2,3],[3,4],[4,5]]
	# print( s.findMinArrowShots(points) )

	points = [[1,2]]
	# print( s.findMinArrowShots(points) )

	points = [[2,3],[2,3]]
	# print( s.findMinArrowShots(points) )

	points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
	print( s.findMinArrowShots(points) )
