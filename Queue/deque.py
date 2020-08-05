from collections import deque

lst = [1,2,3,4,5]
q = deque(lst)

# pop from left
print( q.popleft() )
print( q )
# pop from right
print( q.pop() )
print( q )
# append to right
q.append(5)
# append to left
q.appendleft(1)
print( q )
