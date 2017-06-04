import sys
import math

def secant(func, interval_start, interval_end, iterations):
	#verifies if input is valid
	if (interval_start == interval_end):
		return interval_start

	if interval_start > interval_end:
		#inverts interval if necessary
		temp = interval_start
		interval_start = interval_end
		interval_end = temp

	x = interval_start
	y1 = eval(func)
	x = interval_end
	y2 = eval(func)

	if iterations <= 0 or y1 >= 0 or y2 <= 0:
		#returns whichever value is closest to the root
		if math.fabs(y1) <= math.fabs(y2):
			return interval_start
		return interval_end

	x = 0 #declaring auxiliary variables
	y3 = 0 #declaring auxiliary variables

	#executes secant method
	for i in range(iterations):
		x = interval_start - ((interval_end - interval_start) * y1) / (y2 - y1)
		y3 = eval(func)
		
		#print(str(interval_start) + " " + str(x) + " " + str(interval_end))
		#verifies if root
		if y3 == 0: 
			print("ITERATIONS: " + str(i + 1))
			return x

		#verifies if machine precision was reached
		if x == interval_start:
			print("ITERATIONS: " + str(i + 1))
			return x
		elif x == interval_end:
			print("ITERATIONS: " + str(i + 1))
			return x

		#continues secant method
		if y3 < 0:
			interval_start = x
			y1 = y3
			continue

		interval_end = x
		y2 = y3

	print("ITERATIONS: " + str(i + 1))
	#verifies which value is closest to the root
	#does this because, depending on the values it may enter an
	#infinite loop an never get closer to the root
	x = interval_start
	y1 = eval(func)
	x = interval_end
	y2 = eval(func)
	if math.fabs(y1) <= math.fabs(y2):
		return interval_start
	return interval_end



if len(sys.argv) != 5:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the function
	interval_start = float(sys.argv[2])
	interval_end = float(sys.argv[3])
	iterations = int(sys.argv[4])

	with open(filename) as file:
		func = file.read()
	file.close()
	print(secant(func, interval_start, interval_end, iterations))