"""
Question: https://leetcode.ca/2021-12-16-2093-Minimum-Cost-to-Reach-City-With-Discounts/

"""

from typing import List
import heapq

class Solution:
    def minimumCost(self, n: int, E: List[List[int]], d: int) -> int:
        # prepare a bidirectional graph - bidirectional highway
        G = [{} for _ in range(n)]
        for u, v, w in E:
            G[u][v] = w
            G[v][u] = w
        # init a dist matrix with each node a inf initially
        dist = [[float("inf") for _ in range(n)] for _ in range(d + 1)]
        def dijkstra(i):
            # heapq have only source vertex each time with dist = 0
            # also mark the dist of source as 0 
            pq = [(0, 0)]
            dist[i][0] = 0
            while pq:
                # pull the minimum distance vertex from heap
                cost, u = heapq.heappop(pq)
                # if the current cost of that vertex is more than 
                # the existing cost of the vertex then ignore current 
                # entry in heap 
                if cost > dist[i][u]:
                    continue
                # visit all neighbour of the current node
                for v, w in G[u].items():
                    # keep : cost without considering discount on current edge
                    keep = cost + w
                    # use : cost with discount on current edge - do this only 
                    # when we have atleast one discount available
                    use = dist[i - 1][u] + w // 2 if i > 0 else float("inf")
                    # choose the minimum of two: keep or use
                    newCost = min(use, keep)
                    # update the heap with new item if the current edge 
                    if dist[i][v] > newCost:
                        dist[i][v] = newCost
                        heapq.heappush(pq, (dist[i][v], v))
        # getting minimum dist from source (0 here) to target (n-1 here)
        # each time with a a increased value of discount
        for i in range(d + 1):
            dijkstra(i)
        return dist[d][n - 1] if dist[d][n - 1] != float("inf") else -1



if __name__ == "__main__":
    n = 5
    d = 1
    edges = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]
    s = Solution()
    # nodes -> 0  1  2  3   4
    #         _______________
    # d = 0  | 0  4  7  10  12
    # d = 1  | 0  2  5  8  9
    print(s.minimumCost(n, edges, d))
