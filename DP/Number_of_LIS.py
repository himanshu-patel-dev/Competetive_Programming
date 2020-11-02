class Solution(object):
	def findNumberOfLIS(self, nums):
		N = len(nums)
		if N <= 1: return N

		# len is actually the dp which holds the length of longest
		# subsequence possible till length i is given by length[i]
		lengths = [0] * N 

		# count is the vector which holds the value corresponding to each
		# index i that how many many seq of len dp[i] are seen by now
		#count[i] = number of longest ending in nums till nums[i]
		counts = [1] * N 

		# from 2nd to last number in nums
		for i in range(N):
			# for all num before current number
			for j in range(i):
				# if preceding nums are less than current num
				if nums[j] < nums[i]:
					# then check if we can make current longest seq even 
					# longer by considering number at pos i after seq obtain
					# till index j 
					if lengths[j] >= lengths[i]:
						# it its so then inc the len of longest seq obtained 
						# till index j by 1 and assign it ot index i
						lengths[i] = 1 + lengths[j]

						# also assign the total such sequence possible till 
						# index i is same as total seq available till index j  
						counts[i] = counts[j]
					elif lengths[j] + 1 == lengths[i]:
						# if len of seq at index is already high enough that it
						# can't be inc further but can be achieved through a diff
						# combination then add count of that combination too
						counts[i] += counts[j]

		# len of max possible 
		longest = max(lengths)

		# sum of all combination which will give max seq len is the ans
		return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


if __name__ == "__main__":
	s = Solution()

	lst = [1,3,5,4,7]
	print( s.findNumberOfLIS(lst) )

	lst = [1,2,1,3,2,4,4,5]
	print( s.findNumberOfLIS(lst) )

	lst = [2,2,2,2,2]
	print( s.findNumberOfLIS(lst) )

	lst = [1,2,4,3,5,4,7,2]
	print( s.findNumberOfLIS(lst) )
