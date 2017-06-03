import sys
import mod_op_signs


if len(sys.argv) < 5:
	print("Invalid number of arguments. Read the instruction.md file")

else:
	filename = sys.argv[1] #file storing the function
	x = float(sys.argv[2]) #initial X
	i = float(sys.argv[3]) #pace
	m = int(sys.argv[4]) #number of iteractions

	#generates function from file
	with open(filename) as file:
		content = file.read() #reads file. it should have only one line
	file.close()
	func = content.split(' ') #stores function
	func = [float(x) for x in func] #converts elements from str to float
	func = func[::-1] #inverts function so it can be properly processed

	print(mod_op_signs.bracket_function(func, x, i, m))