"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2

Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""

class Solution:
    def get_element(self,grid,element):
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == element:
                    return (i,j)
        return None
    
    def uniquePathsIII(self, grid):
        for row in grid:
            print(row)

        self.result = 0
        start = self.get_element(grid,1)
        row = len(grid)
        col = len(grid[0])

        if not start:
            return 0

        self.recursive_find(grid,start,row,col)
        return self.result

    def recursive_find(self,grid,start,n,m):
        x,y = start[0], start[1]
        if grid[x][y] == 2:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        return
            self.result += 1
            return

        if y > 0 and (grid[x][y-1] == 0 or grid[x][y-1] == 2):
            t = grid[x][y]
            grid[x][y] = -2
            self.recursive_find(grid,(x,y-1),n,m)
            grid[x][y] = t
        
        if y < m-1 and (grid[x][y+1] == 0 or grid[x][y+1] == 2):
            t = grid[x][y]
            grid[x][y] = -2
            self.recursive_find(grid,(x,y+1),n,m)
            grid[x][y] = t
        
        if x > 0 and (grid[x-1][y] == 0 or grid[x-1][y] == 2):
            t = grid[x][y]
            grid[x][y] = -2
            self.recursive_find(grid,(x-1,y),n,m)
            grid[x][y] = t
        
        if x < n-1 and (grid[x+1][y] == 0 or grid[x+1][y] == 2):
            t = grid[x][y]
            grid[x][y] = -2
            self.recursive_find(grid,(x+1,y),n,m)
            grid[x][y] = t
        


if __name__ == "__main__":
    s = Solution()
    lst = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print( s.uniquePathsIII(lst) )

    lst = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    print( s.uniquePathsIII(lst) )
        
    lst = [[0,1],[2,0]]
    print( s.uniquePathsIII(lst) )
