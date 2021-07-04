"""
In a array nums of size 2 * n, there are n + 1 unique elements, and exactly 
one of these elements is repeated n times. Return the element repeated n times.

Input: nums[1,2,3,3]
Output: 3

Input: nums[2,1,2,5,3,2]
Output: 2

Input: nums[5,1,5,2,5,3,5,4]
Output: 5
"""

from typing import *

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, 4):
            for j in range(n - i):
                if nums[j] == nums[j + i]:
                    return nums[j]

if __name__ == "__main__":
    s = Solution()
    
    nums = [1,2,3,3]
    print(s.repeatedNTimes(nums))

    nums = [2,1,2,5,3,2]
    print(s.repeatedNTimes(nums))

    nums = [5,1,5,2,5,3,5,4]
    print(s.repeatedNTimes(nums))
