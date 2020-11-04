import math

class Point:
	def __init__(self,x,y):
		''' point object '''
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"({self.x} {self.y})"

	@staticmethod
	def distance(a,b):
		''' return distance bw two points '''
		return math.sqrt( (a.x - b.x)**2 + (a.y - b.y)**2 )

def Closest_Inner(points):
	''' returns the min possible distance between all the points '''

	n = len(points)
	if n <= 1:
		raise Exception("Less than 2 points")

	elif n == 2:
		return [points[0], points[1], Point.distance(points[0], points[1])]

	elif n == 3:
		a, b, c = points[0], points[1], points[2]
		d1 = Point.distance(a, b)
		d2 = Point.distance(a, c)
		d3 = Point.distance(b, c)
		
		if d1 <= d2 and d1 <- d3:
			return [a,b,d1]
		elif d2 <= d1 and d2 <= d3:
			return [a,c,d2]
		else:
			return [b,c,d3]

	# partition into two halfs
	left_points = points[:n//2]
	right_points = points[n//2:]

	# for each partition get the min distance bw any two points
	la, lb, dl = Closest_Inner(left_points)
	ra, rb, dr = Closest_Inner(right_points)

	# min distance bw all points in left and right half 	
	if dl < dr:
		ma, mb, d = la, lb, dl
	else:
		ma, mb, d = ra, rb, dr
	
	# get the median line of x axis
	if n%2 == 0:
		mid = ( points[n//2].x + points[n//2-1].x )/2
	else:
		mid = points[n//2].x

	# filter out only required points in range of strip mid-d to mid+d from median
	strip = list( filter( lambda p: mid-d <= p.x <= mid+d, points) )

	localMini = d
	result = [ma, mb, d]
	l = len(strip)
	for i in range(l):
		for j in range( i+1,min(i+7,l) ):
			a,b = strip[i], strip[j]

			if abs(a.y - b.y) > d:
				break

			if Point.distance(a,b) < localMini:
				localMini = Point.distance(a,b)
				result = [a,b, localMini]
	return result


def Closest_Outer(points):
	''' returns the min possible distance between all the points '''
	# sort first on basis of x coordiante and then on y
	points.sort()
	# make point object from tuples
	points = [ Point(p[0],p[1]) for p in points]

	# get the two points which are closest
	res =  Closest_Inner(points)
	
	# return the tuple form of points with min distance
	# format: min distance possible among all pair, first point, sec point
	return [ round(res.pop(), 5) ] + [ (p.x,p.y) for p in res ]

if __name__ == "__main__":
	points = [ (2,3), (12,30), (40,50), (5,1), (12,10), (3,4) ]
	print( Closest_Outer(points) )

	points = [ (1,2), (0,0), (3,6), (4,7), (5,5), (8,4), (2,9), (4,5), 
	(8,1), (4,3), (3,3) ]
	print( Closest_Outer(points) )

	points = [ (1,2), (10,10), (10,4), (-1,-2) ]
	print( Closest_Outer(points) )

	points = [ (1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4), (3,1), 
	(3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4), (5,1), (5,2), (5,3), (5,4), ]
	print( Closest_Outer(points) )
