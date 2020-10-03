"""
There are N gas stations along a circular route, where the amount of gas at 
station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
from station i to its next station (i+1). You begin the journey with an empty 
tank at one of the gas stations.

Return the starting gas station's index (zero based) if you can travel around 
the circuit once in the clockwise direction, otherwise return -1.

Note:
If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. 
Your gas is just enough to travel back to station 3.


Input: 
gas  = [2,3,4]
cost = [3,4,3]
Output: -1

Explanation:
total sum of gas required is more than what we have
"""

class Solution:
	def canCompleteCircuit(self, gas, cost):
		n = len(cost)
		gain = [ gas[i] - cost[i] for i in range(n) ]
		
		# if total gain is less than zero means we can not complete tour
		if sum(gain) < 0:
			return -1
		
		# now its sure that we can complete tour we can start from any 
		# position and track at what time our tank have min capacity as 
		# that is bottelneck we need to cross, to cross that we just 
		# start from index next to it 
		
		# note: individual gain may be -ve but overall gain is 0 or +ve
		
		# here we cal the capacity of tank at each station when we start
		# at index 0 and find the bottelneck
		for i in range(1,n):
			gain[i] += gain[i-1]
			
		result = gain.index( min(gain) )
		return (result+1)%n
		
if __name__ == "__main__":
	s = Solution()
	gas = [1,2,3,4,5]
	cost = [3,4,5,1,2]
	print( s.canCompleteCircuit(gas,cost) )

	gas = [5,8,2,8]
	cost = [6,5,6,6]
	print( s.canCompleteCircuit(gas,cost) )

	gas = [2,3,4]
	cost = [3,4,3]
	print( s.canCompleteCircuit(gas,cost) )
