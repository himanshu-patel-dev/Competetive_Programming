"""
Delete array elements which are smaller than next or become smaller

Input       : arr[] = {20, 10, 25, 30, 40}
              k = 2
Output      : 25 30 40
Explanation : First we delete 10 because it follows
              arr[i] < arr[i+1]. Then we delete 20
              because 25 is moved next to it and it
              also starts following the condition.
"""
def delete_next_greater_element(lst,k):
	n = len(lst)
	stack = []

	for i in range(n):	
		while k and stack and stack[-1] < lst[i]:
			stack.pop()
			k -= 1
		stack.append(lst[i])

	return stack

if __name__ == "__main__":
	lst = [20,10,25,30,45]
	k = 2
	print( delete_next_greater_element(lst,k) )