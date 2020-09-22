""" 
All ele in lst are in range 0 to n-1 
"""
def count_freq(lst):
	n = len(lst)

	for i in range(n):
		pos = lst[i]%n
		lst[pos] += n
	
	for i in range(n):
		print(f"freq of {i} : {lst[i]//n} ")

if __name__ == "__main__":
	lst = [2,5,1,6,2,4,7,3,4]
	count_freq(lst)