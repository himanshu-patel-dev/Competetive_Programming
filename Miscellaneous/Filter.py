lst = [1,2,3,4,5,6]

# filter return only those ele for which expression gives true
res =  filter(lambda x: x%2 == 0 , lst)
print( list(res) )

# filter return only those ele for which expression gives false
res = filter(lambda x: x%2 != 0 , lst)
print( list(res) )