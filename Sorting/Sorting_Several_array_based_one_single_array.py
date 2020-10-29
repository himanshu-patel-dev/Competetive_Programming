'''
	Sort three list based on first list
'''
list1 = ["c", "b", "d", "a"]
list2 = [2, 3, 1, 4]
list3 = [10.5, 25.8, 79.4, 12.6]

# zip all list, a 1st tuple contains first ele of all list
zipped_lists = zip(list1, list2, list3)

# sort each tuple based on which ever list you want
sorted_pairs = sorted(zipped_lists)

# zip all list seperately, here all first ele form one list, all second
# ele form second list and so on
tuples = zip(*sorted_pairs)

# assign all list back to their variables
list1, list2, list3 = [ list(tuple) for tuple in  tuples]

print(list1)
print(list2)
print(list3)
