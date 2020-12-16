def  max_Sum_with_no_Adjacent_item(lst):
    """
    Same as max contiguous sum but no adjacent element should be selected
    """
    n = len(lst)
    dp = [0]*n
    dp[0] = lst[0]
    dp[1] = max(lst[0],lst[1])
    for i in range(2,n):
        if  dp[i-1] > dp[i-2] + lst[i]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-2] + lst[i]

    # print(dp)
    return dp[-1]

    
if __name__ == "__main__":
	lst = [-2, 3, -16, 100, -4, 5]
	print( max_Sum_with_no_Adjacent_item(lst) )