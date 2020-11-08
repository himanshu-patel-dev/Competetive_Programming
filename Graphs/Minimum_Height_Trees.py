'''
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes 
ai and bi in the tree, you can choose any node of the tree as the root. When you select 
a node x as the root, the result tree has height h. Among all possible rooted trees, 
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Leetcode: https://leetcode.com/problems/minimum-height-trees/
'''

class Solution:
	def findMinHeightTrees(self, n, edges):
		if n <= 2:
			return [i for i in range(n)]
		
		# adj list to store neighbour
		neighbour = [set() for i in range(n)]
		# put edges into graph
		for start, end in edges:
			neighbour[start].add(end)
			neighbour[end].add(start)

		# initialize first layer of leaves
		leaves = []
		for v in range(n):
			if len(neighbour[v]) == 1:
				leaves.append(v)

		# keep removing the leaves til we reach the	centroid
		remaining_nodes = n
		while remaining_nodes > 2:
			# remaining points left after removing leaves
			remaining_nodes -= len(leaves)
			new_leaves = []

			# while leaves are present keep looping
			while leaves:
				leaf = leaves.pop()
				# remove leaf in all the its neighbour 
				for n in neighbour[leaf]:
					neighbour[n].remove(leaf)
					# if n is leaf then append it to new leaves
					if len(neighbour[n]) == 1:
						new_leaves.append(n)
			# repeat for new leaves
			leaves =  new_leaves
		return leaves


if __name__ == "__main__":
	s = Solution()

	lst = [[3,0],[3,1],[3,2],[3,4],[5,4]]
	n = 6
	print( s.findMinHeightTrees(n,lst) )