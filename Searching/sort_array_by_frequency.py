lst = [3, 3, 6, 6, 6, 5, 5, 8]

# sort first by count then b value
print(  sorted(lst, key = lambda x: (lst.count(x), x), reverse = True) )

# sort just by count and not by value
print(  sorted(lst, key = lst.count, reverse = True) )
