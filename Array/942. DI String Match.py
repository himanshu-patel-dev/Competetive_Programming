"""
A permutation perm of n + 1 integers of all the integers in 
the range [0, n] can be represented as a string s of length 
n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
"""

from typing import *

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = [0] * (n + 1)
        index = 0

        start, end = 0, n
        for i in range(n):

            # when I then we can put smallest number and next if 
            # I or D wil adjuct accordingly
            if s[i] == 'I':
                result[index] = start
                start += 1 
            # when D then put largest number and next if I is already dealt with
            # and if D then also it will be lower than current number
            else:
                result[index] = end
                end -= 1
            index += 1
            print(start, end)

        result[index] = start
        return result


if __name__ == "__main__":
    sol = Solution()

    s = "IDID"
    print(sol.diStringMatch(s))

    s = "III"
    print(sol.diStringMatch(s))

    s = "DDI"
    print(sol.diStringMatch(s))
