"""
You are given equations in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating-point number). Given 
some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will 
result in no division by zero and there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        G = defaultdict(dict)
        # making graph out of dictionary
        for (x,y),v in zip(equations,values):
            G[x][y] = v
            G[y][x] = 1/v

        # display graph
        # for k,v in G.items():
            # print(k,'->',v)

        return [ self.BFS(x,y,G) for x,y in queries ]

	# DFS can also be used and give same result
    def BFS(self,src,dest,G):
        if src not in G or dest not in G:
            return -1

        # seen holds the node we have seen in bfs as then are not dest
        seen = set()
        # initialize queue with product available
        q = deque( [(src,1)] )

        while q:
            u, prod = q.popleft()
            # if current node is dest than the prod is the required ans
            if u == dest:
                return prod
            seen.add(u)

            # iterating over keys of dictionary and not 
            # visiting already visited nodes else it will create a loop
            for v in G[u]:
                if v not in seen:
                    q.append( (v, prod*G[u][v]) )
        return -1
                



if __name__ == "__main__":
    eq = [["a","b"],["b","c"]]
    val = [2.0,3.0]
    q = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    s = Solution()
    print( s.calcEquation(eq,val,q) )

    eq = [["a","b"],["b","c"],["bc","cd"]]
    val = [1.5,2.5,5.0]
    q = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    s = Solution()
    print( s.calcEquation(eq,val,q) )

    eq = [["a","b"]]
    val = [0.5]
    q = [["a","b"],["b","a"],["a","c"],["x","y"]]
    s = Solution()
    print( s.calcEquation(eq,val,q) )