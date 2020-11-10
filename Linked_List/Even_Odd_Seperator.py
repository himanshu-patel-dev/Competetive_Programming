'''
Seperate even and odd no in LL such that even occur at front and odd in end

T = O(n)
S = O(1)
'''

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

def even_odd(head):
	even_end = odd_end = even_start = odd_start = None

	while head:
		# even no
		if head.data%2 == 0:
			if not even_end:
				even_start = head
				even_end = head
			else:
				even_end.next = head
				even_end = even_end.next
		# odd no
		else:
			if not odd_end:
				odd_start = head
				odd_end = head
			else:
				odd_end.next = head
				odd_end = odd_end.next
		head = head.next
	
	odd_end.next = None
	even_end.next = odd_start
	return even_start


if __name__ == "__main__":
	head = None
	for ele in [8,7,6,5,4,3,2,1]:
		head = insert_beginning(head,ele)
	print_list(head)

	new = even_odd(head)
	print_list(new)