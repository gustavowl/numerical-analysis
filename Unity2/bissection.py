import sys
import mod_bissection

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
	print(mod_bissection.bissection(func, interval_start, interval_end, iterations))