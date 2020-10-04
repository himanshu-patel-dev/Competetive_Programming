import heapq
class PQNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value	# heapify basesd on value

    # compares the second value
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str("{} : {}".format(self.key, self.value))

# a list of nodes
lst = [PQNode(1, 4), PQNode(7, 4), PQNode(6, 9), PQNode(2, 5)]
# heapify the list
heapq.heapify(lst)

# just to see how ele in side list get arranged
print(list(map(str,lst)))

# pop the elements and see they follow min heap based on value
while (lst):
    print (heapq.heappop(lst))