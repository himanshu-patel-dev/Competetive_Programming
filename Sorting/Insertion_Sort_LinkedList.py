class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def insertionSortList(self, head):
		if not head:
			return
		
		# take first node of LL in new LL
		NewHead = head
		# update head LL
		head = head.next
		# break first node from head
		NewHead.next = None
		
		# pick each node from its position and insert it 
		# into new sorted LL
		while head:
			# take current node
			CurrNode = head
			# make head point to next node
			head = head.next
			# delete current node from LL
			CurrNode.next = None
			
			# put curr node in sorted LL
			NewHead = self.insert_into_linkedlist(NewHead,CurrNode)        
		
		return NewHead
			
			
	def insert_into_linkedlist(self,head,Node):
		prev = None
		temp = head

		# iterate while value in sorted LL is less than curr node
		while temp and temp.val < Node.val:
			prev, temp = temp, temp.next
		

		if prev is None:
			Node.next = head
			return Node
		
		prev.next, Node.next = Node, temp

		return head
		
if __name__ == "__main__":
	
	'''
	Input: 4->2->1->3
	Output: 1->2->3->4
	'''

	a = ListNode(4)
	b = ListNode(2)
	c = ListNode(1)
	d = ListNode(3)
	
	a.next = b
	b.next = c
	c.next = d
	
	s = Solution()

	head = s.insertionSortList(a)

	while head.next:
		print(head.val,end='->')
		head = head.next
	print(head.val)