import sys

def transpose(matrix):
	return [[matrix[i][j] for i in range(len(matrix))]
		for j in range(len(matrix[0]))]

def mult_matrix(matrix_a, matrix_b):
	#multiplies matrices. matrixA x matrixB
	result = [[0] * len(matrix_b[0])] * len(matrix_a) #declares result matrix
	#number of columns and rows is not verified

	rows_matrix_a = len(matrix_a)
	cols_matrix_b = len(matrix_b[0])
	rows_matrix_b = len(matrix_b)

	for i in range(rows_matrix_a): #supposes that matrix has at least 1 row
		row = []
		for j in range(cols_matrix_b):
			val = 0
			for k in range(rows_matrix_b):
				val += matrix_a[i][k] * matrix_b[k][j]
			row.append(val)
		result[i] = row
	return result

def apply_f(matrix, x):
	y = [0.0 for i in x] #declares new list
	n = len(matrix) - 1
	#computes values for each row
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			#y[i] += matrix[i][j] * x[i] ** (n - j)
			y[i] = eval(matrix[i])
	print("Y:" + str(y))
	return y

def copy_matrix(matrix):
	return [[x for x in y] for y in matrix]
#start_x is a list containing a guess for the solution
def broyden(matrix, x, max_iterations):
	#creates identity matrix
	matrix_b = [[0.0 for x in range(len(matrix))] for y in range(len(matrix))]
	for i in range(len(matrix)):
		matrix_b[i][i] = 1.0
	matrix_b_inv = copy_matrix(matrix_b)

	for i in range(max_iterations):
		temp = apply_f(matrix, x)
		temp2 = [0.0 for x in range(len(temp))]
		for j in range(len(temp)):
			for k in range(len(temp)):
				temp2[j] += matrix_b_inv[j][k] * temp[k]
		print("temp2: " + str(temp2))
		new_x = [x[i] - temp2[i] for i in range(len(x))]
		print("new_x: " + str(new_x))
		print("ITERATIONS: " + str(i + 1))

		temp2 = apply_f(matrix, new_x)
		delta_f = [[temp2[j] - temp[j]] for j in range(len(temp))]
		print("delta_f: " + str(delta_f))

		delta_x = [[new_x[i] - x[i]] for i in range(len(x))]
		print("delta_x: " + str(delta_x))

		#calculates u. temp = u
		temp = mult_matrix(matrix_b, delta_x)
		temp = [[delta_f[i][0] - temp[i][0]] for i in range(len(delta_f))]
		print("tea: " + str(temp))
		temp2 = 1 / mult_matrix(transpose(delta_x), delta_x)[0][0]
		print("temp2: " + str(temp2))
		temp = [[temp[i][j] * temp2 for j in range(len(temp[i]))]
			for i in range(len(temp))]
		print("yugi: " + str(temp))

		#Bap = Bap + u*transpose(delta_x) UPDATING RULE
		temp2 = mult_matrix(temp, transpose(delta_x))
		matrix_b = [[matrix_b[i][j] + temp2[i][j] for j in range(len(temp2[i]))]
			for i in range(len(temp2))]

		#calculates new inverse
		#Bap**(-1) = Baux**(-1) - (Baux**(-1) * u * transpose(delta_x) * Baux**(-1)) /
		# (1 + transpose(delta_x) * Baux**(-1) * u)
		temp2 = mult_matrix(mult_matrix(matrix_b_inv, temp2), matrix_b_inv)
		print("\n\n\n\n")
		#print(temp2)
		temp = 1 + mult_matrix(mult_matrix(transpose(delta_x), matrix_b_inv), temp)[0][0]
		matrix_b_inv = [[matrix_b_inv[i][j] - temp2[i][j] / temp
			for j in range(len(temp2[i]))] for i in range(len(temp2))]


		print(mult_matrix(matrix_b, matrix_b_inv))

		x = new_x
	return x


if len(sys.argv) != 4:
	print("Invalid number of arguments. Read the instruction.md file")
else:
	matrix_filename = sys.argv[1]
	guess_filename = sys.argv[2]
	max_iterations = int(sys.argv[3])

	matrix = []
	with open(matrix_filename) as file:
		content = file.readlines()
	file.close()
	content = [x.strip() for x in content] #removes '\n' char from the end of line
	for i in range(len(content)):
		matrix.append(content[i])
	#print(matrix)

	guess = []
	with open(guess_filename) as file:
		temp = file.read().split()
		guess = [float(x) for x in temp]
	file.close()

	#print(guess)
	"""
	y = [1.5, 3.5]
	#z = [[1, 0, 1],[1, 2,1],[2,2,2]]
	z = ["x[0]**2 + x[0]*x[1] - 10", 
		"x[1] + 3*x[0]*x[1]**2 - 57"]
	"""
	x = broyden(matrix, guess, max_iterations)
	print("Result: " + str(x))
	for i in range(len(x)):
		print("\tEvaluates eq[" + str(i) + ']' + str(eval(matrix[0])))