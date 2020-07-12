MAX = float('inf')

def print_matrix(dp):
    for row in dp:
        print(*row)

def  Matrix_Multiplication_DP(p):
    n = len(p) - 1
    dp = [ [ 0 for i in range(n) ] for j in range(n)]

    # cl is the chain length, ranges from 0 to n-1
    for cl in range(1,n):
        # i range from as follow
        # i = 1 to 3
        # i = 1 to 2
        # i = 1 to 1
        for i in range(1,n-cl+1):
            # when i = 1, 2, 3 and cl = 1 then j = 2, 3, 4  
            # (1,2) (2,3) (3,4)
            j = i+cl
            dp[i-1][j-1] = MAX
            for k in range(i,j):
                q = dp[i-1][k-1] + dp[k][j-1] + p[i-1]*p[k]*p[j]
                dp[i-1][j-1] = min( dp[i-1][j-1], q )
    print_matrix(dp)
    return dp[0][-1]

if __name__ == "__main__":
	p = [ 1,2,1,4,1]
	print( Matrix_Multiplication_DP(p) )
