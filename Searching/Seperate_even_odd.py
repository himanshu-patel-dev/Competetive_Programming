"""
Given a lst of integers seperate even in front and odd in end
its not requied to maintaining relative ordering

also seperatin a lst of 0s and 1s with all 0 in front and 1s in end

solve in single scan of lst. T = O(n)
"""

def seperate(lst):
	n = len(lst)
	front, end = 0, n-1

	while front < end:
		# reach odd ele from front
		while front<n and lst[front]%2 == 0:
			front += 1
		# reach even ele form last
		while end>0 and lst[end]%2:
			end -= 1

		if front < end:
			# swap the elemetents
			lst[front], lst[end] = lst[end], lst[front]
			front += 1
			end -= 1
		else:
			break

	return lst

if __name__ == "__main__":
	lst = [12, 34, 45, 9, 8, 90, 3]
	print( seperate(lst) )

	lst = [0,1,0,1,0,1,1,0,0]
	print( seperate(lst) )