'''
LeetCode: https://leetcode.com/problems/increasing-order-search-tree/solution/

Given the root of a binary search tree, rearrange the tree in in-order so that 
the leftmost node in the tree is now the root of the tree, and every node has 
no left child and only one right child.
'''

'''
Solution:
T = O(n)	n = number of nodes in tree
S = O(h) 	h = height of tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            node.left = None
            
            self.head.right = node
            self.head = node
            
            inorder(node.right)
            
        
        ans = self.head = TreeNode(None)
        inorder(root)
        return ans.right

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
