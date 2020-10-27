"""
Given a linked list 
1. Detect whether there is a cycle
2. Find the node where the the tail of linked list ends

In T = O(n)
and S = O(1)

"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# tell whether there is a cycle or not if there is a cycle the 
	# give the node where the fast and slow meet 
	def isCycle(self,slow,fast):
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
			
			if slow == fast:
				return slow
		return False
	
	def detectCycle(self, head):
		if not head:
			return None
		
		# get the node where the fast and slow meet
		cycle = self.isCycle(head,head)
		if not cycle:
			return None
		
		# now the distace of junction (point where the tail meet the LL back)
		# is same from start node and node where fast and slow meet

		# proof:
		# dist moved by slow = x+y
		# dist moved by fast = 2x + 2y
		# extra moved by fast = x+y
		# fast move y in loop before slow enters loop and after 
		# moving x more it will reach junction as we dont know value of 
		# x here we start another pointer from start and move both 1 pos 
		# at a time till we reach junction  

		start = head
		Count = 1
		while start != cycle:
			cycle = cycle.next
			start = start.next
			Count += 1
		
		return Count
		
if __name__ == "__main__":
	s = Solution()
	
	node_1 = ListNode(1)
	node_2 = ListNode(2)
	node_3 = ListNode(3)
	node_4 = ListNode(4)
	# node 4 points back to node 2
	node_1.next = node_2
	node_2.next = node_3
	node_3.next = node_4
	node_4.next = node_2

	print( s.detectCycle(node_1) )
