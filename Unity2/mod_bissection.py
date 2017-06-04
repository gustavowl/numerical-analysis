import math

def bissection(func, interval_start, interval_end, iterations):
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

	#executes bissection method
	for i in range(iterations):
		x = (interval_start + interval_end) / 2
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

		#continues bissection
		if y3 < 0:
			interval_start = x
			continue

		interval_end = x

	print("ITERATIONS: " + str(i + 1))
	return x