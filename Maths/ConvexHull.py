class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def get_start(lst,n):
	"""
	it give the left most point among all points
	it is the start point of convex hull
	"""
	mini = 0
	for i in range(1,n):
		if lst[mini].x > lst[i].x:
			mini = i
		elif lst[mini].x == lst[i].x and lst[mini].y < lst[i].y:
			mini = i
	return mini

def orientation(a,b,c):
	"""
	return orientation of order tuple a,b,c
	return 0 if colinear
	return 1 if clockwise
	return 2 if anticlockwise
	"""
	val = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y)
	if val > 0:
		return 1
	elif val < 0:
		return 2
	else:
		return 0

def ConvexHull(lst):
	"""
	also called jarvis algo
	returns the points from lst which are required for making convex hull
	time comp = O(n^2) or O(n*w) , w = num of points in boundary of convex hull
	spae comp = O(n)
	"""
	n = len(lst) 
	if n < 3:
		return None

	start = get_start(lst,n) 
	hull = set()
	p = start

	while True:
		hull.add(p)
		q = (p+1)%n

		for i in range(n):
			if orientation( lst[p], lst[i], lst[q] ) == 2:
				q = i
		p = q
		if p == start:
			break

	# hull contains only index of selected points
	points = []
	for i in hull:
		points.append( (lst[i].x, lst[i].y) )
	return sorted(points)


if __name__ == "__main__":
	n = int(input())
	t = []
	for i in range(n):
		a,b = map(int, input().split())
		t.append( (a,b) )

	# removing duplicates in points
	t = list(set(t))
	n = len(t)
	if n < 3:
		print("Not Convex Hull")

	# making pair of coordiantes to point object
	for i in range(n):
		t[i] = point( t[i][0], t[i][1] )

	print( ConvexHull(t) )

"""
15
34 36
20 28
16 12
1 2
38 25
37 48
38 34
36 40
21 25
20 19
44 25
26 2
40 45
3 2
46 22 
"""
