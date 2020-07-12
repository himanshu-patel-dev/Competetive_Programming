def ways_to_end_of_matix(n,m):
    """
    ways to go to end of matrix only down and right move are allowed
    """
    dp = [ [1 for i in range(m)] for j in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

for _ in range(int(input())):
    a,b = map(int, input().split())
    print( ways_to_end_of_matix(a,b) )