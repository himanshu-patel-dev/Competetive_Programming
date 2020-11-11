'''
Given the coordinates of four points in 2D space, 
return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an 
integer array with two integers.

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

'''

'''
Solution:

T = O(1)
S = O(1)
'''

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        # print(p1, p2, p3, p4)
        
        def dist(a,b):
            # eucledian distance
            return abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2
        
        # all sides equal then rombus
        a = dist(p1,p2)
        b = dist(p2,p4)
        c = dist(p4,p3)
        d = dist(p3,p1)
        
        # diag equal then rectangle
        diag1 = dist(p2,p3)
        diag2 = dist(p1,p4)
        
        if a != 0 and a == b and b == c and c == d and d == a and diag1 == diag2:
            return True
        return False

    
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(P, Q):
            return (P[0] - Q[0])**2 + (P[1] - Q[1])**2

        D = [dist(p1, p2), dist(p1, p3), dist(p1, p4),
             dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        D.sort()
        
        # diag = sqrt(2) * side
        # diag^2 = 2 * side ^ 2
        
        return 0 < D[0] == D[1] == D[2] == D[3] and 2*D[0] == D[4] == D[5]