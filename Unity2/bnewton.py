import mod_bissection
import mod_newton
import sys

if len(sys.argv) != 7:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	function_filename = sys.argv[1] #file storing the function in format evaluatable by eval()
	interval_start = float(sys.argv[2])
	interval_end = float(sys.argv[3])
	iterations_bissection = int(sys.argv[4])
	#file storing the derivative function in format evaluatable by eval()
	derivative_filename = sys.argv[5]
	iterations_newton = int(sys.argv[6])

	with open(function_filename) as file:
		func = file.read()
	file.close()

	with open(derivative_filename) as file:
		dfunc = file.read()
	file.close()

	x = mod_bissection.bissection(func, interval_start, interval_end, iterations_bissection)
	print("Bissection: " + str(x) + "\n")

	x = mod_newton.newton(func, dfunc, x, iterations_newton)
	print("Newton: " + str(x))