"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1
otherwise return 0.

2.5 is not "two and a half" or "half way to version three", it is 
the fifth second-level revision of the second first-level revision.


Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"

"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))

        n1, n2 = len(v1),len(v2)
        
        for i in range(max(n1,n2)):
            first = v1[i] if i < n1 else 0
            second = v2[i] if i<n2 else 0
            
            if first > second:
                return 1
            elif first < second:
                return -1
        return 0