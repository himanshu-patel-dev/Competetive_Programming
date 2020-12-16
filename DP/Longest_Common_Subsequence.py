def  Longest_Common_Subsequence(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    dp = [ [0 for i in range(n1+1)] for j in range(n2+1) ]
    
    for i,x in enumerate(string1):
        for j,y in enumerate(string2):
            if x == y:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max( dp[i][j+1], dp[i+1][j] )
        
    # use this return to get the max len of LCS
    # return dp[n1][n2]

    for row in dp:
        print(row)

    # to get the actual LCS string
    result = ""
    while n1 != 0 and n2 != 0:
        if dp[n1][n2] == dp[n1-1][n2]:
            n1 -= 1
        elif dp[n1][n2] == dp[n1][n2-1]:
            n2 -= 1
        else:
            result = string1[n1-1] + result
            n1 -= 1
            n2 -= 1
    return result

if __name__ == "__main__":
    string1 = "abcde"
    string2 = "bdefg"
    print( Longest_Common_Subsequence(string1,string2) )