'''
Given the array nums, for each nums[i] find out how many numbers 
in the array are smaller than it. That is, for each nums[i] you have 
to count the number of valid j's such that j != i and nums[j] < nums[i].

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100

Return the answer in an array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
'''

class Solution:
    '''
        find the first index of given ele in a sorted array
        do this for all element in given array and return those 
        indexes 

        T = O(nlogn)
        S = O(n)
    '''
    def first(self, arr, low, high, target, n) :
        if(high >= low) :
            mid = (low+high)//2
            # if the element at mid is same as target

            match = arr[mid] == target
            no_smaller_to_left = ( mid == 0 or target > arr[mid - 1])
            
            if( match and no_smaller_to_left ) :
                return mid
            
            elif(target > arr[mid]) :
                return self.first(arr, (mid + 1), high, target, n)
            
            else :
                return self.first(arr, low, (mid - 1), target, n)
        
        return -1

    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        n = len(nums)
        
        return [ self.first(sorted_nums, 0, n-1, ele, n) for ele in nums]


class Solution:
    '''
        Make an array of size equal the size of maximum possible size of given integer in array
        Make a prefix sum array for each element's count and take count of element 1 less then it

        T = O(n)
        S = O(1) .. array is constant
    '''
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        res = [0]*n
        prefix_sum = [0]*101

        # count occurance
        for k in nums:
            prefix_sum[k] += 1

        # make prefix sum
        for i in range(len(prefix_sum)-1):
            prefix_sum[i+1] += prefix_sum[i]
        
        # get the elements less than curr ele
        for i in range(n):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = prefix_sum[nums[i]-1]
        return res



if __name__ == "__main__":
    s = Solution()

    nums = [8,1,2,2,3]
    print(s.smallerNumbersThanCurrent(nums))
