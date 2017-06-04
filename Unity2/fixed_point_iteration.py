import sys
import math

"""
evaluates a function for an specified value
this differs from mod_op_signs.function since the last evaluates a
given polynomial, not a function.
Also, the format of how the function if represent is different.
The function most be in a format understanble by python, for example:
	(x+10)^(1/2)/x
would be written as
	math.pow(x+10, 1/2)/x
"""

def fixed_point(func, x, epsolon, iterations):
	x1 = 0
	epsolon = math.fabs(epsolon)
	for i in range(iterations):
		x1 = eval(func)
		#check if with desired precision
		if math.fabs(x - x1) <= epsolon:
			print("ITERATIONS: " + str(i + 1))
			return x1
		x = x1
	print("ITERATIONS: " + str(iterations))
	return x


if len(sys.argv) != 5:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the fixed point function to be evaluated
	x = float(sys.argv[2]) #initial guess for x
	epsolon = float(sys.argv[3]) #desired precision
	iterations = int(sys.argv[4]) #max number of iterations

	with open(filename) as file:
		func = file.read() #reads file. it should have only one line
	file.close()

	print(fixed_point(func, x, epsolon, iterations))

	#test root of x^4-x-10