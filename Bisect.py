#insert element in a sorted array to maintain sort
#insert element to left or right of group of element similar to its own

import bisect

lst = [9,5,12,5,8,7,1,25]
print("Unsorted: ",lst)
lst.sort()  #best method to sort
print("Sorted: ",lst)

#Index of given num in sorted list(from left if repeted)
print("1: ", bisect.bisect_left(lst,5) )    

#(Index+1) of given num in sorted list(from right if repeted)
print("2: ", bisect.bisect_right(lst,5) )   

#index in sorted where num can be inserted
print("3: ", bisect.bisect(lst,6) )

# index of place where 5 can be inserted (used to count num less than or equal to given num)
print("4: ", bisect.bisect(lst,5) )

#insert in list to sorted position (return nothing)
bisect.insort(lst, 10)
print("5: ",  lst)

#insert at sorted position from left (not mdifferend from previous)
bisect.insort_left(lst, 5)
print("6: ",lst)

#insert at sorted position from right (specifing begining and ending position)
bisect.insort_right(lst, 10, 0, 3)
print("7: ",lst)
