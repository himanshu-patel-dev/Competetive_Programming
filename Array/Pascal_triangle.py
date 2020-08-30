"""
return nth row of pascal triangle
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

T = O(n^2)

for T = O(n) use binomial coefficient 5C0 5C1 5C2 5C3 5C4 5C5
"""

def pascal_triangle(n):
	lst = [1]

	for i in range(2,n+1):
		temp = lst[::] + [1]

		for j in range(1,i-1):
			temp[j] += lst[j-1]
		lst = temp

	return lst

if __name__ == "__main__":
	n = 4
	print( pascal_triangle(n) )