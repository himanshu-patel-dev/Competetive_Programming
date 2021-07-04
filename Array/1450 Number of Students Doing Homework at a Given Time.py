"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished 
it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, 
return the number of students where queryTime lays in the interval [startTime[i], 
endTime[i]] inclusive.

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't 
doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also 
wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the 
only student doing homework at time 4.
"""

from typing import *

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = max(endTime)
        studentStudying = [0] * (n + 1)

        for s, e in zip(startTime, endTime):
            studentStudying[s - 1] += 1
            studentStudying[e] += 1

        # prefix sum
        for i in range(1, n):
            studentStudying[i] += studentStudying[i - 1]

        return studentStudying[queryTime - 1]

if __name__ == "__main__":
    s = Solution()

    startTime = [1,2,3]
    endTime = [3,2,7]
    queryTime = 4
    print(s.busyStudent(startTime, endTime, queryTime))
