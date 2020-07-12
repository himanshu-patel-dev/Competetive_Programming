import math

# trunc is used for truncating fractional part
a = 3.141
print( math.trunc(a) )	# output 3

# can be used for checking a number is integer or nort
var = 5.16
print( var == math.trunc(var) )

var = 4.00000
print( var == math.trunc(var) )
