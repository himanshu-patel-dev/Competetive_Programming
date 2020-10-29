import heapq

def optimal_merge(lst):
	heapq.heapify(lst)

	while len(lst) > 1:
		# pop two min ele from priority queue 
		a = heapq.heappop(lst)
		b = heapq.heappop(lst)
		# append the sum of both back to queue
		heapq.heappush(lst,a+b)
	
	return lst[0]

if __name__ == "__main__":
	lst = [5,10,15,20,50,100]
	print( optimal_merge(lst) )

	lst = [2, 3, 4, 5, 6, 7]
	print( optimal_merge(lst) )