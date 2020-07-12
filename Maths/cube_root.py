def cube_root(n):
	if n > 0:
		return round(n**(1/3) , 4)
	else:
		return - round( (-n)**(1/3), 4)

if __name__ == "__main__":
	# n = 64
	n = 125
	print( cube_root(n) )