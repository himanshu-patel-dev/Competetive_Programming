'''
Given an array of positive integers arr, calculate the 
sum of all possible odd-length subarrays.
Return the sum of all odd-length subarrays of arr.

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
'''

class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0
        prefix_sum = [0]
        for ele in arr:
            prefix_sum.append( ele + prefix_sum[-1] )
        
        # actual array =  [1,4,2,5,3]
        # prefix sum = [0,1,5,7,12,15]

        # react every possible combination by using two loops
        for i in range(n):
            for j in range(i,n):
                length = j-i+1      # length bw two end points
                
                if length%2 != 0:   # if length is odd add the total of those two end point
                    total += prefix_sum[j+1] - prefix_sum[i]
        return total


if __name__ == "__main__":
    s = Solution()

    nums = [1,4,2,5,3]
    print(s.sumOddLengthSubarrays(nums))
