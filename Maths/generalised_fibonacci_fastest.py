# for taking mod of result
m = 0
def fib(n,a,b,c,first,sec):
    """
    first term of fibo sequence
    sec term of fibo sequence
    nth term f(n) = a*f(n-1) + b*f(n-2) + c
    """
    F = [ [a,b,c],[1,0,0], [0,1,0] ]
    if n == 1:
        return first
    elif n == 2:
        return sec
    else:
        F = power(F, n-2,a,b,c)
        return (F[0][0]*sec+ F[0][1]*first + F[0][2])%m
 
def power( F, n,a,b,c):
    if n == 1:
        return F
    C = power(F,n//2,a,b,c)
    C = matrix_multiply(C,C)
    if n%2:
        M = [ [a,b,c],[1,0,0],[0,1,0] ]
        return matrix_multiply(C,M)
    else:
        return C

def matrix_multiply(A,B):
    mul = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                mul[i][j] += (A[i][k] * B[k][j])%m
            mul[i][j] = mul[i][j]%m
    return mul

if __name__ == "__main__":
    first = 0    
    sec = 1      
    a = b = 1       
    c = 0
    m = 10**10
    for n in range(1,11):
        print( fib(n,a,b,c,first,sec) )