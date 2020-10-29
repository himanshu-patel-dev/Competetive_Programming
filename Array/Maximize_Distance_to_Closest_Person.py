"""
You are given an array representing a row of seats where seats[i] = 1 
represents a person sitting in the ith seat, and seats[i] = 0 represents 
that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the 
closest person to him is maximized. 

Return that maximum distance to the closest person.

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest 
person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

"""

class Solution:
	def maxDistToClosest(self, seats):
		occupied = []
		n = len(seats)

		# get index of first one and this is one option if leading zeros
		front = seats.index(1)
		# get index of last one and this is one option if trainling zeros
		last = seats[::-1].index(1)
		
		diff = 0
		result = 0
		prev = front
		
		for i in range(front+1,n):
			if seats[i] == 0:
				continue  
			
			# get the diff bw two index of 1
			# this diff is used keeping in mind the case when
			# there is only 1 0 in bw two 1's [1,0,1] then diff = 2 (not 3 or 1)
			# and hence result = 2//2 = 1
			diff = max(diff,i-prev)
			# assign half of this as to result
			result = diff//2

			# each time we found a 1 we update the prev location of 1
			prev = i

		
		return max(front, last, result)

if __name__ == "__main__":
	s = Solution()

	seats = [1,0,0,0,1,0,1]
	print( s.maxDistToClosest(seats) )
	
	seats = [1,0,0,0]
	print( s.maxDistToClosest(seats) )
	
	seats = [0,1]
	print( s.maxDistToClosest(seats) )
	