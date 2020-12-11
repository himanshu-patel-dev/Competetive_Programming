'''
Given a sorted array nums, remove the duplicates in-place such 
that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this 
by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer, but your answer 
is an array?
Note that the input array is passed in by reference, which means 
a modification to the input array will be known to the caller.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev_char = 'x'
        j = 0
        
        for i in range(len(nums)):
            nums[j] = nums[i]
            
            if nums[i] == prev_char and count > 1:
                continue
            
            if prev_char == nums[i]:
                count += 1
            else:
                prev_char = nums[i]
                count = 1
            j += 1
            
        return j