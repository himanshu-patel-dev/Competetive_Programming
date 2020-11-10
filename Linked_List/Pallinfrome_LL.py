class Node:
	# constructor for single node
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self) -> str:
		return str(self.data)
	
def insert_end(head,data):
	# inserting node at end
	newNode = Node(data)

	while head.next != None:
		head = head.next
	# no need to return any thinf the LL passed as argument is itself modified
	head.next = newNode

def print_list(head):
	# print entire linked list
	while head.next != None:
		print(head.data,' -> ',end='')
		head = head.next
	print(head.data)

def middle_Node(head):
	slow, fast = head, head
	while fast.next and fast.next.next:
		fast, slow = fast.next.next, slow.next
	return slow

def isPallindrome(head1):
	# get the middle node of LL
	middle = middle_Node(head1)
	current = middle.next
	prev = None


	while current:
		current.next, current, prev = prev, current.next, current
	# seond half of LL in reversed way
	head2 = prev

	# to break the loop bw two half of LL
	middle.next = None
	# print_list(head1)
	# print_list(head2)
	
	# and head1.next != head2 and head2.next != head1
	while head1 and head2:
		if head1.data != head2.data:
			return False
		head1 = head1.next
		head2 = head2.next
	# return for first half equal second half (even)
	# if odd len LL then middle ele is in head1 and need no check
	return True 


if __name__ == "__main__":
	
	# create a LL of even length
	head = Node('a')
	for ele in list('bccba'):
		insert_end(head,ele)
	print_list(head)

	print( isPallindrome(head) )
	
	# create a LL of odd length
	head = Node('a')
	for ele in list('bcdcba'):
		insert_end(head,ele)
	print_list(head)

	print( isPallindrome(head) )

	# create a LL of even length
	head = Node('a')
	for ele in list('bccbx'):
		insert_end(head,ele)
	print_list(head)

	print( isPallindrome(head) )
	
	# create a LL of even length
	head = Node('a')
	for ele in list('bcdeba'):
		insert_end(head,ele)
	print_list(head)

	print( isPallindrome(head) )
	
	