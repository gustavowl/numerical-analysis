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


#starts cholesky decomposition

for i in range(len(matrix)):
	#calculates for matrix[i][i]
	for j in range(i - 1, -1, -1):
		matrix[i][i] -= matrix[j][i] ** 2
	matrix[i][i] = matrix[i][i] ** (1 / 2)

	for j in range(i + 1, len(matrix)):
		for k in range(i - 1, -1, -1):
			matrix[i][j] -= matrix[k][i] * matrix[k][j]
		matrix[i][j] /= matrix[i][i]

#the resulting matrix will correspond to gT. This means that the 
#inferior diagonal matrix is invalid, but can be obtained from the transpose

#to obtain the answer vector x, solve the following:
#1 - Gy = b
#2 - GTx = y

#1 - Gy = b
#obtaining the vector y from b (change the values of b)
for i in range(len(matrix)):
	for j in range(i):
		matrix[i][len(matrix)] -= matrix[j][i] * matrix[j][len(matrix)]
	matrix[i][len(matrix)] /= matrix[i][i]
#2 - GTx = y
#obtaining the vector x from y
for i in range(len(matrix) - 1, -1, -1):
	for j in range(len(matrix) - 1, i, -1):
		matrix[i][len(matrix)] -= matrix[i][j] * matrix[j][len(matrix)]
	matrix[i][len(matrix)] /= matrix[i][i]

print(matrix)