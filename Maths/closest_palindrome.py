def reverse(s):
    return s[::-1]

def closest_palindrome(n):
    """
    return the palindrome close to n that is with min abs( n - pali_num )
    if two num have same difference from n and are palindrome than return the
    least one
    """
    # is n is string remove this line
    string = str(n)

    if string == reverse(string):
        return string
    l = len(string)

    # if l is even it get first half if l is odd it gets first half + middle ele 
    first_half = int( string[: (l+1)//2 ] )

    # sol for case when n = 100 then sol = 99 
    # and when n = 999 then sol = 999 + 2 = 1001
    sol = set( [10**l + 1, 10**(l-1)-1 ] )

    for half in map(str, [ first_half+1, first_half, first_half-1 ]):
        # if half is from odd len array we remove middle ele repetition
        # in second half
        num = half + reverse( half[:-1] if l%2 else half )
        sol.add( int(num) )

    # first selection based on n-x then on basis of x
    return min( sol, key = lambda x: ( abs(n-x), x ) )

for _ in range(int(input())):
    n = int(input())
    print( closest_palindrome(n) )