import math
import sys

def function(f, x): #computes f(x), return it
	y = 0
	
	for i in range(len(f)):
		y += f[i] * x**i
	return y


def bracket_function(func, x, interval, max_iterations):
	#function is must be a list
	y1 = function(func, x)

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

#finds the limit of the function. Either inferior or superior.
#it just applies L = 1 + (B/an)^(1/(n-k))
def find_limit(func):
	n = len(func) - 1
	#print("n = " + str(n))
	if func[0] == 0 or func[n] <= 0:
		#lagrange cannot be applied
		return None
	
	#finds k, the largest index of negative coefficients
	k = 0
	for i in range(n - 1, -1, -1):
		if func[i] < 0:
			k = i
			break
	#print("k = " + str(k))

	#finds b, the absolute value of the smallest coefficientes
	b = func[i]
	for i in range(k - 1, -1, -1):
		if func[i] < b:
			b = func[i]
	b = math.fabs(b)
	#print("b = " + str(b))

	return 1 + (b/func[n]) ** (1/(n-k))

#finds the inferior and superior limits for the roots
def lagrange_bracketing(func):
	#superior limit
	n = len(func) - 1
	if func[n] < 0:
		return None
	sup = find_limit(func)

	#does P1(x) = x^n P(1/x)
	func2 = func[::-1]
	#if an < 0, multiply function by -1
	if func2[n] < 0:
		func2 = [x*-1 for x in func2]
		#print(func2)

	inf = find_limit(func2)
	return [inf, sup]

def lagrange_and_opposite_sign(func, delta):
	interval = lagrange_bracketing(func)
	print("LaGrange bracketing: " + str(interval))
	max_iterations = math.ceil( (interval[1] - interval[0])
		/ delta)

	#print([func, interval[0], delta, max_iterations])
	interval = bracket_function(func, interval[0], 
		delta, max_iterations)

	print ("LaGrange after OppSign: " + str(interval))
	return interval
	



if len(sys.argv) < 3:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the function
	delta = float(sys.argv[2]) #interval precision for opp_sign bracketing
	func = get_function_from_file(filename)
	lagrange_and_opposite_sign(func, delta)