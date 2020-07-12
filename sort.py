#sorting in python

lst = [3,7,1,21,56,23,3,9,6]
print("List: ",lst)

lst.sort()
print("Sorted: ",lst)

lst.sort(reverse = True)
print("Reverse: ",lst)

# sort using desired index
order = lambda x: x[1]
    
lst = [ (1,2), (9,4), (7,10), (21,2) ]

lst.sort(key = order)
print("Sorted: ",lst)

lst.sort(key = order, reverse = True)
print("Reversed: ", lst)