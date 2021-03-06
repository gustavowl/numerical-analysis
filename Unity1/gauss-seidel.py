#generates matrix from file
#the file will be a n x n+1 matrix. where the last column
#contains the b vector
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

#reads initial approximation vector (the guessed solution)
#the vector will be writen in transpose form.
#the vector will have size n+1 where the value of n equals the size n
#of the matrix. n+1 because the last the last element will be the epsilon
#value for approximation of solution and stop condition
guess_vector = []
with open("guess_vector.txt") as file:
	content = file.read()
guess_vector = [eval(x) for x in content.strip().split()]
#extracts epsilon
e = guess_vector.pop()

curr_e = e
while not curr_e < e: #stops when curr_e < e
	print(guess_vector)
	max_x = 0
	max_d = 0
	curr_e = 0
	for i in range(len(matrix)):
		#necessary for calculating max_d. It will restore the value of #previous guess
		temp = guess_vector[i]

		guess_vector[i] = matrix[i][len(matrix)]
		#print(guess_vector[i])
		for j in range(len(matrix)):
			if i != j:
				guess_vector[i] -= matrix[i][j] * guess_vector[j]
				#print('\t' + str(matrix[i][j]) + '*' + str(guess_vector[(index + 1)%2][j]))
		guess_vector[i] /= matrix[i][i]
		#print('\t' + str(matrix[i][i]))
		#print()
		max_x = max(max_x, abs(guess_vector[i]))

		max_d = max(max_d, abs(temp - guess_vector[i]))

	#verifies if solution in guess_vector is satisfactory
	curr_e = max_d / max_x
	#print(guess_vector)
	#print(str(max_d) + ' ' + str(max_x))

print(guess_vector)
