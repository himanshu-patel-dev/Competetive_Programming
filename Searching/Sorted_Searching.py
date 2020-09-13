def sorted_search(lst,target):
	for ele in lst:
		if ele == target:
			return True
		if ele > target:
			return False
	return False

if __name__ == "__main__":
	# sored data
	lst = [1,4,5,7,8,24,27]
	target = 6
	
	if sorted_search(lst,target):
		print("Ele found")
	else:
		print("Ele not found")