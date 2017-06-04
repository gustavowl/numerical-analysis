import math

def bracket_function(func, x, interval, max_iterations):
	#function must be a string evaluatable by eval()
	
	y1 = eval(func)
	print(y1)

	for i in range(max_iterations):
		x += interval
		y2 = eval(func)
		if y1 * y2 <= 0:
			#found the closed interval that constais the root, return it
			if (x - interval < x):
				return [x - interval, x]
			return [x, x - interval]
		#otherwise compute next interval
		y1 = y2
	#else stop method
	return None