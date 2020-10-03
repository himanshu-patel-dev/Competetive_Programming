"""
Sort Linked List Using merge sort
T = O(nlogn)
S = O(1) 
"""

class Node:
	# constructor for single node
	def __init__(self):
		self.data = None
		self.next = None

class Linked_list(Node):
	def __init__(self):
		# initializing linked list with head pointing to None
		self.head = None
		
	def insert(self,data):
		# inserting node at end
		newNode = Node()
		newNode.data = data

		if self.head is None:
			self.head = newNode
			return

		current = self.head
		while current.next != None:
			current = current.next
		current.next = newNode

	def print_list(self):
		# print entire linked list
		current = self.head
		while current.next != None:
			print(current.data,' -> ',end='')
			current = current.next
		print(current.data)


	def get_middle(self,head):
		# if even no of nodes return last node of first half
		# if odd no of nodes return the middle node pointer
		if head is None:
			return None

		slow = fast = head
		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next

		return slow

	def merge_sorted_linkedlist(self,head1,head2):
		# result now points to a dummy node which will be removed later
		# t always points to last node in new Linked List		
		result = Node()
		t = result

		# only when both list have nodes inc the pointer and assign 
		# it a new node from the two, else break loop
		while head1 and head2:
			if head1.data < head2.data:
				t.next = head1
				head1 = head1.next
			else:
				t.next = head2
				head2 = head2.next	
			t = t.next

		# t points to last node in new list 
		# assign it the list which have remaining elements
		if head1:
			t.next = head1
		if head2:
			t.next = head2

		return result.next

	def sort_linked_list(self,head):
		# if empty LL or only one ele is present no sorting is required
		if head is None or head.next is None:
			return head

		# get the node from where we want to split current LL
		mid = self.get_middle(head)
		mid_next = mid.next

		# break the LL into two part from here
		mid.next = None

		# sort both the parts
		left = self.sort_linked_list(head)
		right = self.sort_linked_list(mid_next)
	
		# merge both sorted LL into one and return 
		return self.merge_sorted_linkedlist(left,right)
		

if __name__ == "__main__":
	LL1 = Linked_list()
	LL1.insert(30)
	LL1.insert(10)
	LL1.insert(40)
	LL1.insert(60)
	LL1.insert(50)
	LL1.insert(20)
	LL1.insert(50)
	LL1.print_list()

	# a blank LL
	sorted_LL = Linked_list()
	# sort the LL1 and it will return the head of sorted LL
	sorted_LL.head = LL1.sort_linked_list(LL1.head)
	# put the head as head of new LL
	sorted_LL.print_list()
	