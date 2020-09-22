"""
An integer has sequential digits if and only if each digit in the 
number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] 
inclusive that have sequential digits. 

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

class Solution:
    def __init__(self):
        self.all_result = [1]
        string = '123456789'
        # iterating to get num of all length from 2 to 9
        # each window select all possible numbers
        for window in range(2,10):
            temp = []
            # a widow of 2 will select 12, 23, 34, 45, 56, 67, 78, 89
            for start in range(0,9-window+1):
                temp.append( int( string[start:start+window] ) )
            # append the result to end of all result
            self.all_result.extend(temp)

    def SequentialDigits(self, low, high):
        result = []
        for ele in self.all_result:
            if low <= ele <= high:
                result.append(ele)
            # ele are in sorted order thus as soon ele cross upper 
            # bound break the loop 
            if ele > high:
                break
        return result

if __name__ == "__main__":
    s = Solution()
    low = 100
    high = 300

    print( s.SequentialDigits(low,high) )

    low = 1000
    high = 13000

    print( s.SequentialDigits(low,high) )
        