def triplet_sum(lst,target):
	""" find three index i,j,k such that lst[i] + lst[j] + lst[k] = target """
	""" T = O(n^2 + nlog(n)) = O(n^2) two nested loop """
	lst.sort()
	n = len(lst)

	# fixed the least element in triplet
	for i in range(n-2):
		# choose the other two element using two pointer approch
		l,r = i+1,n-1
		while l<r:
			current_sum = lst[i] + lst[l] + lst[r] 
			if current_sum == target:
				return (lst[i],lst[l],lst[r])
			if current_sum < target:
				l += 1
			else:
				r -= 1
	return "Not Found"


if __name__ == "__main__":
	lst = [4, 3, 45, 10, 6, 11, 8] 
	target = 22
	print( triplet_sum(lst,target) )