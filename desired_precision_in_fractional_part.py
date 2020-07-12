""" print with required precision in fraction """
var = 3.14
# here desired precision = 6 fractional digit
print( "{0:.6f}".format(var) )

# or round of two desired precision
# 1 = 1 fraction digit
print( round(var,1) )
print( round(var,0) )