'''
URL: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

There is an m x n matrix that is initialized to all 0's. 
There is also a 2D array indices where each indices[i] = [ri, ci] 
represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the 
matrix after applying the increment to all locations in indices.

Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
'''

class Solution:
    '''
        Record how many times each row or col is being referred in indices array
        and the sum of both of these referrence is the total of each cell in matrix

        let k = len(indices)
        T = O(mn,k)
        S = O(k)
    '''

    def oddCells(self, m, n, indices):
        # to record how many times a row or col is being referred in indices
        row = [0]*m
        col = [0]*n
        

        # complexity = len(indices)
        # record all row and col referrenced in indices
        for index in indices:
            r,c = index
            row[r] += 1
            col[c] += 1
                    
        count = 0
        # complexity = m*n
        # count of each cell is the sum of it's being referred in cols and rows
        for i in range(m):
            for j in range(n):   
                # count only odd cells
                if (row[i]+col[j])%2 != 0:
                    count += 1
                    
        return count

if __name__ == "__main__":
    s = Solution()

    m,n = 2,3
    indices = [[0,1],[1,1]]
    print(s.oddCells(m,n,indices))
