class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def orientation(a,b,c):
	"""
	0 for collinear
	1 for clockwise
	2 for counter clockwise
	"""
	slope = (b.y-a.y)*(c.x-b.x) - (c.y-b.y)*(b.x-a.x)
	if slope < 0:
		return 2 
	elif slope > 0:
		return 1
	else:
		return 0

def on_segment(a,b,c):
	# check if b is on segment a to c
	x_comp_intersect = False
	y_comp_intersect = False
	
	if b.x >= min( a.x, c.x ) and b.x <= max(a.x, c.x):
		x_comp_intersect = True
	if b.y >= min( a.y, c.y ) and b.y <= max(a.y, c.y):
		y_comp_intersect = True
	return x_comp_intersect and y_comp_intersect

def intersecting(p1,q1,p2,q2):
	"""
	return true if line segment p1 q1 intersect with p2 q2 els false
	"""
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	# first condition check
	if o1 != o2 and o3 != o4:
		return True 
	
	# second condition check
	if o1 == 0 and on_segment(p1,p2,q1):
		return True
	elif o2 == 0 and on_segment(p1,q2,q1):
		return True
	elif o3 == 0 and on_segment(p2,p1,q2):
		return True
	elif o4 == 0 and on_segment(p2,q1,q2):
		return True

if __name__ == "__main__":
	p1 = point(10,0)
	q1 = point(0,10)
	p2 = point(0,0)
	q2 = point(10,10)

	if intersecting(p1,q1,p2,q2):
		print("Intersecting")
	else:
		print("Not Intersecting")

	p1 = point(-5,-5)
	q1 = point(0,0)
	p2 = point(1,1)
	q2 = point(10,10)

	if intersecting(p1,q1,p2,q2):
		print("Intersecting")
	else:
		print("Not Intersecting")