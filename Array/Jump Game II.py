'''
Given an array of non-negative integers nums, you are initially positioned at 
the first index of the array. Each element in the array represents your maximum 
jump length at that position. Your goal is to reach the last index in the minimum 
number of jumps.
You can assume that you can always reach the last index.

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2

Input: nums = [1,1,1,1]
Output: 3
'''

class Solution:
    '''
        Start with start=0 and end=0 and jumps=0 our goal is to reach last index
        we loop till start < last_ind

        Each time start < last_ind we inc jumps by 1 because if are unable to reach last
        index then we need at least one jump. 

        Then we traverse all ele from start index to end index and get the farthest jump
        we can make. and then reassign start and end limits.

        Again if the start do not reached last index we make a jump again. and check again
        have our end index reached or exceeded last_ind in such case return jumps.

        T = O(n)
        S = O(1)
    '''

    def jump(self, nums):
        start = 0
        end = 0
        jumps = 0
        last_ind = len(nums)-1

        while start < last_ind:
            jumps += 1
            max_end = 0
            for i in range(start,end+1):
                max_end = max(max_end, nums[i]+i)
            
                if max_end >= last_ind:
                    return jumps

            start = end+1
            end = max_end
            
        return jumps


if __name__ == "__main__":
    s = Solution()

    m,n = 2,3
    indices = [[0,1],[1,1]]
    print(s.oddCells(m,n,indices))
