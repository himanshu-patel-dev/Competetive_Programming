import heapq

# iterable
lst = [2,4,1,8,6,3]

# convert list into heap queue or priority queue 
# function do not return anything
# in place in linear time
heapq.heapify(lst)
print('Heap: ',lst)

# insert an element into heap
heapq.heappush(lst,10)
print('Heap Push: ',lst)

# pop min element from heap and return it
# if heap is empty then it return an Index Error
print('Heap pop:',heapq.heappop(lst) )
print('Heap after pop: ',lst)

# heap pushpop insert an element and return min ele from heap
# this run fater than a comb of push and then pop
print("Pop and push: ",heapq.heappushpop(lst,12))
print("Heap: ",lst)

# pop then push element to heap
# raise index error if heap is empty
print("Heap replace: ",heapq.heapreplace(lst,0))
print("Heap: ",lst)


# n largest element, in sorted order
# if n is larger than size of heap no index error is shown
print("3 largest Heap element: ", heapq.nlargest(3,lst) )

# n minimum element, in sorted order
# if n is larger than size of heap no index error is shown
print("3 smallest elemet: ",heapq.nsmallest(3,lst))

# get no of elements in heap
print(len(lst))
print(lst)
