class Node:
	# constructor for single node
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

def print_list(head):
	# print entire linked list
	while head.next != None:
		print(head.data,' -> ',end='')
		head = head.next
	print(head.data)

def insert_beginning(head,data):
	# inserting node at beginning
	newNode = Node(data)
	newNode.next = head
	return newNode

def merge_sorted_LL(head1,head2):
	'''
	Return merge LL of two which is sorted
	both input LL are sorted
	T = O( min(n,m) )
	S = O(1)
	'''
	head = Node(0)
	curr = head

	while head1 and head2:
		if head1.data < head2.data:
			curr.next = head1
			head1 = head1.next
		else:
			curr.next = head2
			head2 = head2.next
		curr = curr.next
	head = head.next

	if head1:
		curr.next = head1
	if head2:
		curr.next = head2

	return head

if __name__ == "__main__":
	head1 = None
	for ele in [5,4,3,2,1]:
		head1 = insert_beginning(head1,ele)
	
	head2 = None
	for ele in [20,19,18,17,16]:
		head2 = insert_beginning(head2,ele)

	# two sorted LL
	print_list(head1)
	print_list(head2)

	newLL = merge_sorted_LL(head1, head2)
	print_list(newLL)

