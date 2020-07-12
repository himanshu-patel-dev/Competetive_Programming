def Integer_knapsack(capacity, value, weight):
    if capacity < min(weight):
        return 0
    else:
        ans = []
        n = len(value)
        for i in range(n):
            if capacity >= weight[i]:
                ans.append( 
                    Integer_knapsack(capacity - weight[i], value, weight) 
                    + value[i] 
                    )
        return max(ans)

if __name__ == "__main__":
    capacity = 40
    value = [40, 100, 120]
    weight = [10, 20, 30]
    print( Integer_knapsack(capacity, value, weight) )
