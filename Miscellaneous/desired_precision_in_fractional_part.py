""" print with required precision in fraction """
var = 3.14
# here desired precision = 10 fractional digit
print( "{0:.10f}".format(var) )
print( f"{var:0.10f}" )

# or round of two desired precision
# 1 = 1 fraction digit
print( round(var,1) )
print( round(var,0) )