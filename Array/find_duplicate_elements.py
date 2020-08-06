"""
Find duplicate in an array of size n. 
constarint: 1 <= array[i] <= n
Find in O(n) time and O(1) space
"""

class Solution:
    def findDuplicates(self, nums):
        result = []
        for ele in nums:
            # get absolute of each element it might be 
            # set negative in some operation
            ele = abs(ele)
            # base on magnitude of element calculate index of element
            # given 1 <= ele <= n, so no out of boundary error
            i = ele-1
            # if that index is already negative means current element
            # is a duplicate, add it in result
            if nums[i] < 0:
                result.append(ele)
            else:
                nums[i] = -nums[i]
        return result

if __name__ == "__main__":
	s = Solution()
	print( s.findDuplicates([1,2,3,4,5,2,3]) )