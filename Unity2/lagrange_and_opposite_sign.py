import mod_op_signs
import math

#finds the limit of the function. Either inferior or superior.
#it just applies L = 1 + (B/an)^(1/(n-k))
def find_limit(func):
	n = len(func) - 1
	print("n = " + str(n))
	if func[0] == 0 or func[n] <= 0:
		#lagrange cannot be applied
		return None
	
	#finds k, the largest index of negative coefficients
	k = 0
	for i in range(n - 1, -1, -1):
		if func[i] < 0:
			k = i
			break
	print("k = " + str(k))

	#finds b, the absolute value of the smallest coefficientes
	b = func[i]
	for i in range(k - 1, -1, -1):
		if func[i] < b:
			b = func[i]
	b = math.fabs(b)
	print("b = " + str(b))
	
	return 1 + (b/func[n]) ** (1/(n-k))

find_limit(mod_op_signs.get_function_from_file("function.txt"))