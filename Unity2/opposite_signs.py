import sys
import mod_op_signs


if len(sys.argv) < 5:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the function
	x = float(sys.argv[2]) #initial X
	i = float(sys.argv[3]) #pace
	m = int(sys.argv[4]) #number of iterations

	with open(filename) as file:
		func = file.read()
	file.close()
	
	print(mod_op_signs.bracket_function(func, x, i, m))