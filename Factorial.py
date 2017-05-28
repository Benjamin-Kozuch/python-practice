def factorial(num):
	final_value = 1
	for i in range(1, num + 1):
		final_value *= i
	return final_value



def factorial_using_recursion(num): 

    if num > 1:
        return num * FirstFactorial(num-1)
    else:
        return 1 



print factorial(0)
