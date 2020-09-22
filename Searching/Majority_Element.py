"""
Given an array of size n, find the majority element. The majority element 
is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist 
in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

"""

"""
Solution:

There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.

T = O(n) and S = O(1)
Boyer-Moore Voting Algorithm

If we had some way of counting instances of the majority element as +1
and instances of any other element as -1, summing them would make it obvious 
that the majority element is indeed the majority element.
"""

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for ele in nums:
			# as soon we get a element and count is zero we consider that element 
			# as candidate element
            if count == 0:
                candidate = ele
                
			# inc or dec count of candidate element as per instances seen
            if ele == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate

if __name__ == "__main__":
	s = Solution()

	lst = [3,2,3]
	print( s.majorityElement(lst) )