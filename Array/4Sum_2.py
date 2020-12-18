'''
Given four lists A, B, C, D of integer values, compute how many 
tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 
0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result 
is guaranteed to be at most 231 - 1.
'''

from collections import Counter, defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        first, total = defaultdict(int), 0
        
        A = Counter(A)
        B = Counter(B)
        C = Counter(C)
        D = Counter(D)
        
        for a in A:
            for b in B:
                first[a+b] += A[a]*B[b]
            
        for c in C:
            for d in D:
                if -(c+d) in first:
                    total += C[c]*D[d]*first[-(c+d)]
                
        return total

if __name__ == "__main__":
	s = Solution()

	A = [ 1, 2]
	B = [-2,-1]
	C = [-1, 2]
	D = [ 0, 2]

	print( s.fourSumCount(A,B,C,D) )