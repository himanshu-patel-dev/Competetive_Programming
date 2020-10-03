"""
Given a list of non negative integers, arrange them such that they 
form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string 
instead of an integer.

"""

class Custom_Comparator(str):
    """ Inherit from string class and override the less than comparison method """
    def __lt__(first,second):
        """ return true if num form by concat (+) by first+sec is less than sec+first """
        return first+second < second+first

class Solution:
    def largestNumber(self, nums):      
        if not nums:
            return ""
        nums = list(map(str,nums))
        nums.sort(key = Custom_Comparator, reverse = True)
        
        return ''.join(nums) if nums[0] != '0' else '0'
        

if __name__ == "__main__":
    s = Solution()

    lst = [3,30,34,5,9]
    print( s.largestNumber(lst) )

    lst = [10,2]
    print( s.largestNumber(lst) )

    lst = [9,90,900]
    print( s.largestNumber(lst) )

    lst = [000,0,00]
    print( s.largestNumber(lst) )