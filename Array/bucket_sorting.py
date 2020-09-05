"""
Given an array of integers, find out whether there are two distinct 
indices i and j in the array such that the absolute difference between 
nums[i] and nums[j] is at most t and the absolute difference between 
i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or not nums or k <= 0:
            return False
        # a dict to hold the num which fall in respective bucket
        buckets = {}
        # in each bucket there are t+1 items passible (0,t), (t+1, 2t+1), ...
        width = t + 1 

        for i,n in enumerate(nums):
            print(buckets)
            bucket = n//width

            if bucket in buckets:
                # all elements in buckets are in range 0 to t i.e. we got ans 
                # if atleast two ele match to same bucket 
                return True
            
            # assign current num a bucket
            buckets[bucket] = n

            # it is possible that we do not get two ele in same bucket but two 
            # adj bucket have ele that are well within the range t, this is only 
            # possible in adj bucket
            if bucket-1 in buckets and n - buckets[bucket-1] <= t:
                return True 

            if bucket+1 in buckets and buckets[bucket+1] - n <= t:
                return True
            
            # difference bw two indices at most k thus we delete num bucket which 
            # got beyond a window of k elements
            if i >= k:
                # from i = 0 to i = k the diff in index is within range k
                # as soon i = k we need to remove index 0 ==> k - k = 0
                # so that bucket 0 should not be used in next iteration on k+1
                out_bucket = nums[i-k]//width
                del buckets[out_bucket]

        # if nothig matches return False
        return False


if __name__ == "__main__":
    s = Solution()

    print( s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) )

    # print( s.containsNearbyAlmostDuplicate([1,2,3,1],3,0) )

    # print( s.containsNearbyAlmostDuplicate([1,0,1,1],1,2) )

    # print( s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) )
