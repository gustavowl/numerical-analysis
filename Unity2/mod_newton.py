import math

def newton(func, dfunc, x, iterations):
	#executes newton method
	old_x = x
	y = eval(func)
	for i in range(iterations):
		x = x - y / eval(dfunc)
		y = eval(func)

		#verifies if root
		if y == 0: 
			print("ITERATIONS: " + str(i + 1))
			return x

		#verifies if machine precision was reached
		if x == old_x:
			print("ITERATIONS: " + str(i + 1))
			return x

		#continues execution
		old_x = x

	print("ITERATIONS: " + str(i + 1))
	return x