from collections import defaultdict
def pythogoras_triplet(lst):
	""" return element a,b,c from lst which have rel a^2 + b^2 = c^2 """
	n = len(lst)
	lst.sort()
	# sq every element
	lst_sq = [ ele*ele for ele in lst] 
	dct = defaultdict(int)
	
	for i in range(n):
		dct[ lst_sq[i] ] = i

	for i in range(n-1):
		for j in range(i+1,n):
			hyp = lst_sq[i] + lst_sq[j]
			if hyp in dct and dct[hyp] > j:
				return (lst[i],lst[j], lst[ dct[hyp] ] )
			if hyp > lst[-1]:
				break
	return "Not Found"

lst = [3,5,1,2,4]
print( pythogoras_triplet(lst) )

lst = [3,7,1,2,4]
print( pythogoras_triplet(lst) )
