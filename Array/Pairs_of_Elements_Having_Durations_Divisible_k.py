'''
You are given a list of songs where the ith song has a 
duration of time[i] seconds.

Return the number of pairs of songs for which their total 
duration in seconds is divisible by 60. Formally, we want 
the number of indices i, j such that i < j with 
(time[i] + time[j]) % 60 == 0.

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500

'''

class Solution:
	def numPairsDivisibleBy60(self, time):
		time = [ num%60 for num in time]
		
		count = [0]*60
		for ele in time:
			count[ele] += 1

		total = count[0]*(count[0]-1)//2
		for i in range(1,30):
			total += max( count[i], count[60-i] ) * min( count[i], count[60-i] )
		
		total += count[30]*(count[30]-1)//2
		
		return total

class Solution:
	def numPairsDivisibleBy60(self, time):
		from collections import defaultdict
		remainders = defaultdict(int)
		ret = 0
		for t in time:
			if t % 60 == 0: # check if a%60==0 && b%60==0
				ret += remainders[0]
			else: # check if a%60+b%60==60
				ret += remainders[60-t%60]
			remainders[t % 60] += 1 # remember to update the remainders
		return ret

if __name__ == "__main__":
	s = Solution()

	lst = [30,20,150,100,40]
	print(s.numPairsDivisibleBy60(lst))

	lst = [60,60,60]
	print(s.numPairsDivisibleBy60(lst))
