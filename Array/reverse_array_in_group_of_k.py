"""
Reverse array in groups. Given an array arr[] of positive 
integers of size N. Reverse every sub-array of K group elements

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}

Output: 3 2 1 5 4
Explanation: Reversing groups in size k = 3, first group consists 
of elements 1, 2, 3. Reversing this group, we have elements in 
order as 3, 2, 1. then reverse remaining 4 anf 5 as 5 4.

"""

def reverseInGroups(A,N,K):
    for i in range(0,N,K):
        j = min(N,i+K)
        # print(A)
        A = A[:i] + A[i:j][::-1] + A[j:]
    return A

if __name__ == "__main__":
	lst = [1,2,3,4,5]
	print( reverseInGroups(lst,5,3) )

	lst = [5,6,8,9]
	print( reverseInGroups(lst,5,3) )
