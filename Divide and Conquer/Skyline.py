'''
Leetcode: https://leetcode.com/problems/the-skyline-problem/

Two approch 
1. Divide and Conquer T= O(nlogn) S = O(n)
2. Priority Queue T= O(nlogn) S = O(n)
'''

class Solution:
	def getSkyline(self, buildings):
		''' T = O(nlogn) S = O(n) '''
		return self.getSkyline_rec(0, len(buildings)-1, buildings)

	def getSkyline_rec(self,low, high, buildings):
		''' make a recursice call with reduced input size '''
		Skyline = []

		if low > high:
			return Skyline
		elif low == high:
			# if only one building in input then return its skyline
			x1, x2, h = buildings[low]
			Skyline.append( [x1,h] )
			Skyline.append( [x2,0] )
			return Skyline
		else:
			# two recusive call with left an right half
			mid = (low+high)//2
			Skyline_lower = self.getSkyline_rec(low, mid, buildings)
			Skyline_upper = self.getSkyline_rec(mid+1, high, buildings)
			return self.merge_skyline(Skyline_lower, Skyline_upper)

	def merge_skyline(self, Skyline_lower, Skyline_upper):
		i, j, h1, h2 = 0, 0, 0, 0
		Merged_Skyline = []

		while i<len(Skyline_lower) and j<len(Skyline_upper):
			first = Skyline_lower[i]
			second = Skyline_upper[j]

			# comparing both intervals based on x coordinates
			# select the one with lower x coordinate

			if first[0] < second[0]:
				# new hight is the max out of current skyline coord or prev skyline 
				# coord because it prev skyline is not finised yet and current skyline
				# can inc or dec max height 
				Merged_Skyline.append( [first[0], max( first[1], h2 )] )
				h1 = first[1]	# update the prev seen height of curr skyline
				i += 1

			elif second[0] < first[0]:
				Merged_Skyline.append( [second[0], max(h1, second[1])] )
				h2 = second[1]	# update the prev seen height of curr skyline
				j += 1

			else:
				Merged_Skyline.append( [first[0], max(first[1], second[1])] )
				h1, h2 = first[1], second[1]
				i += 1
				j += 1

		# put the remaining skyline of lower
		while i < len(Skyline_lower):
			Merged_Skyline.append( Skyline_lower[i] )
			i += 1
		# put the remaining skyline of upper
		while j < len(Skyline_upper):
			Merged_Skyline.append( Skyline_upper[j] )
			j += 1

		# remove the redundent skyline by checking if only x coord differ and 
		# height is same then reject those entries
		result = []
		for line in Merged_Skyline:
			if not result:
				result.append( line )
				continue
			
			if result[-1][1] != line[1]:
				result.append( line )
		return result


if __name__ == "__main__":
	s = Solution()

	# format [ x, y, height ]
	buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
	res = s.getSkyline(buildings)
	print( res )
