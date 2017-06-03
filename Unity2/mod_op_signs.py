def function(f, x): #computes f(x), return it
	y = 0
	
	for i in range(len(f)):
		y += f[i] * x**i
	return y


def bracket_function(func, x, interval, max_iteractions):
	#function is must be a list
	
	y1 = function(func, x)

	for i in range(max_iteractions):
		x += interval
		y2 = function(func, x)
		if y1 * y2 <= 0:
			#found the closed interval that constais the root, return it
			if (x - interval < x):
				return [x - interval, x]
			return [x, x - interval]
		#otherwise compute next interval
		y1 = y2
	#else stop method
	return None