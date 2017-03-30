#generates matrix from file
with open("matrix.txt") as file:
	content = file.readlines() #saves each line to content.
	#content is a vector of lines, i.e. each line is an element
#print(content)
content = [x.strip() for x in content] #removes '\n' char from the end of line
matrix = [] #declares variable
#generates matrix from content, i.e. list of list
for i in range(len(content)):
	matrix.append([eval(n) for n in content[i].split()]) #also converts to float list
#ends matrix generation

#starts L.U. decomposition. It will change the original matrix
#L will have unitary(?) diagonal, hence it is not represented
#the matrix input has the following property: col = row +1, i.e, has one extra column
#this extra column reprets the b vector, which is the "desired solution"
for i in range(len(matrix)):
	max_index = i
	#identifies which row contains the biggest element at column i
	for j in range(i + 1, len(matrix)):
		if (abs(matrix[max_index][i]) < abs(matrix[j][i])):
			max_index = j
	#swap i-th row with max_index-th row
	row = matrix[max_index]
	matrix[max_index] = matrix[i]
	matrix[i] = row
	
	#applying Gauss
	for row in range(i+1, len(matrix)):
		for col in range(i, len(matrix)):
			if (col == i):
				matrix[row][col] /= matrix[i][col]
			else:
				matrix[row][col] -= matrix[i][col] * matrix[row][i]

#prints compact L.U. Matrix along with the b vector
print(matrix)

#calculates y from Ly = b
#executes foward substitution (changes b vector)
#since L[0][0] is = 1, loop starts at 1
for i in range(1, len(matrix)):
	for j in range(i-1, -1, -1):
		matrix[i][len(matrix)] -= matrix[i][j] * matrix[j][len(matrix)]
print(matrix)

#calculates Ux = y
#executes back substitution (changes b vector)
#b vector will contain the values for solution

for i in range(len(matrix) - 1, -1, -1):
	for j in range(len(matrix) - 1, i-1, -1):
		if (j == i):
			matrix[i][len(matrix)] /= matrix[j][j]
		else:
			matrix[i][len(matrix)] -= matrix[i][j] * matrix[j][len(matrix)]
print(matrix)