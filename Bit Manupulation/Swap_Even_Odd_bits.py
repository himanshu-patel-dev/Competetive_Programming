def swap(n):
	'''
	swap even num bits (from right) with left num bits (from left)
	n = 0000 1010 => 0101

	n = 0000 1111 => 
	even = 1010 => 0101  
	odd = 0101 => 1010
	n = 0101 | 1010 = 1111
	'''
	even_bits = n & 0xAAAA
	odd_bits = n & 0x5555
	even_bits = even_bits >> 1
	odd_bits = odd_bits << 1
	return even_bits | odd_bits

if __name__ == "__main__":
	n = 10
	print( swap(n) )

	n = 15
	print( swap(n) )