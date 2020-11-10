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

def remove_duplicate_adj(head):
	newhead = head
	t = newhead
	while head:
		if t.data != head.data:
			t.next = head
			t = t.next
		head = head.next
	
	# break the LL at end
	t.next = None
	return newhead

if __name__ == "__main__":
	head = None
	for ele in [5,5,5,4,4,3,3,3,2,2,1,1]:
		head = insert_beginning(head,ele)
	print_list(head)

	new = remove_duplicate_adj(head)
	print_list(new)
