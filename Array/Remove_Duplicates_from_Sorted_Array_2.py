'''
Given a sorted array nums, remove the duplicates in-place such 
that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.
'''


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        first = 0
        
        for i in range(len(nums)):
            if nums[first] != nums[i]:
                first += 1
                nums[first] = nums[i]

        return first+1

if __name__ == "__main__":
    s = Solution()

    nums = [1,1,2]
    print(s.removeDuplicates(nums))
    print(nums)

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))
    print(nums)
