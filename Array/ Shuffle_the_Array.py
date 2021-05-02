'''
Given the array nums consisting of 2n elements in the form 
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
'''

# solution 1
class Solution:
    '''
        make a new array of len 2n and put all first n ele in it's even places
        and next n ele in odd places of new array
        
        T = O(2n) = O(n)
        S = O(2n) = O(n)
    '''
    def shuffle(self, nums, n):
        result = [0]*2*n 

        for i in range(n):
            result[2*i] = nums[i]       # for even places
            result[2*i+1] = nums[i+n]   # for odd places

        return result

# solution 2
class Solution:
    '''
        swap the number in same array. Put each number in its desired position
        and mark it -ve and keep doing this till we make all number -ve.
        
        T = O(2n) = O(n)
        S = O(1) Inplace 
    '''
    def shuffle(self, nums, n):
        desiredIndex = lambda i: 2*i if i<n else (i-n)*2+1 

        # let's iterate for all numbers atleast once
        for i in range(2*n):
            j = i
            # while current number is +ve it's not in it's place
            while nums[i] >= 0:
                # get the desired position for element which was originally at j'th place
                j = desiredIndex(j)
                # swap i'th and j'th position element
                nums[i], nums[j] = nums[j], -nums[i]

        for i in range(2*n):
            nums[i] = -nums[i]

        return nums



if __name__ == "__main__":
    s = Solution()

    nums = [2,5,1,3,4,7]
    n = 3
    print(s.shuffle(nums, n))
