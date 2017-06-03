def function(f, x): #computes f(x), return it
	y = 0
	
	for i in range(len(f)):
		y += f[i] * x**i
	return y


def bracket_function(func, x, interval, max_iterations):
	#function is must be a list
	
	y1 = function(func, x)
	print(y1)

	for i in range(max_iterations):
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

def get_function_from_file(filename):
	#generates function from file
	with open(filename) as file:
		content = file.read() #reads file. it should have only one line
	file.close()
	func = content.split(' ') #stores function
	func = [float(x) for x in func] #converts elements from str to float
	return func[::-1] #inverts function so it can be properly processed