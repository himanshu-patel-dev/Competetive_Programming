import math
def y_is_power_of_x(x,y):
	"""
	return true if y is a power of x i.e y = x**p
	"""
	if x == 1:
		return y == 1

	p = int(math.log(y,x))
	if x**p == y:
		return True
	else:
		return False

if __name__ == "__main__":
	a,b = 2,8
	print(y_is_power_of_x(a,b))