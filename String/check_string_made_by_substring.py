"""
Given a non-empty string check if it can be constructed by taking a substring 
of it and appending multiple copies of the substring together. You may assume 
the given string consists of lowercase English letters only and its length will 
not exceed 10000.

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Input: "aba"
Output: False

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""

from collections import defaultdict
from math import gcd 

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        Just check all posible divisors of lenght of s, 
        replicate them and compare them with original string.
        """
        N = len(s)
        # len of substring = i in range 1 to N//2
        # if len of i > N//2 then its not substring
        # if for any value of i we get N%i == 0 it means 
        # it can be a subtring, check by replicating s[:i] (sub string)
        # (N//i) number of times  

        # Time Comp = O(n*sqrt(n)) as there there are sqrt(n) num which 
        # divide N, then for comparing all N ele with s it take N time
        for i in range(1,N//2+1):
            if N%i == 0 and s[:i]*(N//i) == s:
                return True
        return False


if __name__ == "__main__":

    s = Solution()
    print( s.repeatedSubstringPattern('abab') )

    print( s.repeatedSubstringPattern('aba') )

    print( s.repeatedSubstringPattern('abcabcabcabc') )
