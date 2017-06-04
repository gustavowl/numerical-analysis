import sys
import mod_op_signs
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

	y1 = mod_op_signs.function(func, interval_start)
	y2 = mod_op_signs.function(func, interval_end)

	if iterations <= 0 or y1 >= 0 or y2 <= 0:
		#returns whichever value is closes to the root
		if math.fabs(y1) <= math.fabs(y2):
			return interval_start
		return interval_end

	new_x = 0 #declaring auxiliary variables
	y3 = 0 #declaring auxiliary variables

	#executes bissection
	for i in range(iterations):
		new_x = (interval_start + interval_end) / 2
		y3 = mod_op_signs.function(func, new_x)

		
		#print(str(interval_start) + " " + str(new_x) + " " + str(interval_end))
		#verifies if root
		if y3 == 0: 
			print("ITERATIONS: " + str(i + 1))
			return new_x

		#verifies if machine precision was reached
		if new_x == interval_start:
			print("ITERATIONS: " + str(i + 1))
			return new_x
		elif new_x == interval_end:
			print("ITERATIONS: " + str(i + 1))
			return new_x

		#continues bissection
		if y3 < 0:
			interval_start = new_x
			continue

		interval_end = new_x

	print("ITERATIONS: " + str(i + 1))
	return new_x



if len(sys.argv) != 5:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the function
	interval_start = float(sys.argv[2])
	interval_end = float(sys.argv[3])
	iterations = int(sys.argv[4])

	func = mod_op_signs.get_function_from_file(filename)
	print(bissection(func, interval_start, interval_end, iterations))




