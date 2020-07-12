p = 1000000007

def fib(n,a,b):
    """
    return n th fibo numvber where n >= 1
    a = first term and b = second term 
    fastest = O( log(n) )
    """
    F = [ [1,1],[1,0] ]
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        F = power(F, n-2)
        return F[0][0]*b + F[0][1]*a

def power( F, n ):
    if n == 1:
        return F
    C = power(F,n//2)
    C = matrix_multiply(C,C)
    if n%2:
        M = [ [1,1],[1,0] ]
        return matrix_multiply(C,M)
    else:
        return C

def matrix_multiply(A,B):
    a = ( A[0][0]*B[0][0] + A[0][1]*B[1][0] )%p
    b = ( A[0][0]*B[0][1] + A[0][1]*B[1][1] )%p
    c = ( A[1][0]*B[0][0] + A[1][1]*B[1][0] )%p
    d = ( A[1][0]*B[0][1] + A[1][1]*B[1][1] )%p
    return [ [a,b], [c,d] ]

if __name__ == "__main__":
# for _ in range(int(input())):
    a = 1
    b = 1
    n = int(input())
    print( fib(n,a,b)%p )