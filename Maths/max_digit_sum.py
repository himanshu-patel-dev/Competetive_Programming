def digit_sum(n):
	s = 0
	while n:
		s += n%10
		n = n//10
	return s

def max_digit_sum(n):
	"""
	find no in range 1 to n digit sum is max , if many print the largest
	"""
	ans = n
	max_sum = digit_sum(n)

	string = str(n)
	l = len(string)
	for i in range(l):
		if string[i] != '0':
			num =  string[:i] + str(int(string[i])-1) + '9'*(l-i-1)
			num = int(num)
			d = digit_sum(num)
		if d > max_sum or d == max_sum and num > ans:
			ans = num
			max_sum = d
	return ans

if __name__ == "__main__":
	for _ in range(int(input())):
		n = int(input())
		print( max_digit_sum(n) )