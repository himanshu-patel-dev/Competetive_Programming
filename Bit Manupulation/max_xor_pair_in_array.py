def findMaximumXOR(nums):
    ans, mask = 0,0

    for bit in range(31,-1,-1):
        # get the new mask it will help us to get required 
        # prefix from all the numbers in array
        # mask = 1000...., 1100...., 1110...., 1111.... 
        mask = mask | (1<<bit)

        # all the number with only prefix bits as there are set bits in mask
        prefix_set = { ele & mask for ele in nums}
        
        # start is the new ans we desired to get, if any two prefix xor give
        # start as a result we upgrade the ans
        # basically we try to inc the value of ans with 1 set bit each time 
        start = ans | (1<<bit)
        for prefix in prefix_set:
            # do not worry about the case when start ^ prefix = prefix and
            # while making a lookup we hit prefix itself and 
            if start ^ prefix in prefix_set:
                ans = start
                break
    return ans


if __name__ == "__main__":
    # max xor 25 ^ 5 = 28
    lst = [3,10,5,25,2,8]
    print( findMaximumXOR(lst) )