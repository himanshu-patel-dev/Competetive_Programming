def  Max_Sum_No_Adjacent_item(lst):
    """
    Same as max contiguous sum but no adjacent element should be selected
    """
    n = len(lst)
    M = [0]*n
    M[0] = lst[0]
    M[1] = max(lst[0],lst[1])
    for i in range(2,n):
        if M[i-1] > M[i-2] + lst[i]:
            M[i] = M[i-1]
        else:
            M[i] = M[i-1] + lst[i]
    return M[-1]

    
if __name__ == "__main__":
	lst = [-2, 3, -16, 100, -4, 5]
	print( Max_Sum_No_Adjacent_item(lst) )