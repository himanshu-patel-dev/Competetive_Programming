'''
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
 Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
'''

class Solution:
	'''
		T = O(n)
		S = O(1)

		Moving from point A to point B take time equal to max( abs diff in x coordinated, abs diff in y coordinates )

	'''
	def minTimeToVisitAllPoints(self, points):
		total = 0
		start = points[0]			# starting points is same as first point in array
		for dest in points[1:]:	
			# get the abs difference in btw x and y coord
			x = abs(start[0]-dest[0])	
			y = abs(start[1]-dest[1])
			
			# max of those diff is the amount of time we required 
			total += max(x,y)
			start = dest
		return total

if __name__ == "__main__":
	s = Solution()

	points = [[1,1],[3,4],[-1,0]]
	print(s.minTimeToVisitAllPoints(points))
