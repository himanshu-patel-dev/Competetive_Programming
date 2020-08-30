"""
Given a sorted array having 10 elements which contains 6 
different numbers in which only 1 number is repeated five times. 
Your task is to find the duplicate number using two comparisons only.
"""
for _ in range(int(input())):
	a = list(map(int, input().split()))
	if a[3] == a[4]:
		print(a[3])
	elif a[4] == a[5]:
		print(a[4])
	else:
		print(a[5])
