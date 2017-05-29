#You will be given an array with 5 numbers. 
#The first 2 numbers represent a range, and the next two numbers represent another range. 
#The final number in the array is X. 
#The goal of your program is to determine if both ranges overlap by at least X numbers. 
#For example, in the array [4, 10, 2, 6, 3] the ranges 4 to 10 and 2 to 6 overlap by at least 3 numbers (4, 5, 6), 
#so your program should return true.


def overlap(arr):

	overlaped = "false"
	list1 = range(arr[0],arr[1]+1)
	list2 = range(arr[2],arr[3]+1)
	threshhold = arr[4]
	numbers_in_both_l1_and_l2 = 0

	for i in list1:
		if i in list2:
			numbers_in_both_l1_and_l2 += 1

	if numbers_in_both_l1_and_l2 >= threshhold:
		overlaped = "true"
	
	return overlaped



print overlap([4, 10, 2, 5, 3])
print overlap([4, 10, 2, 5, 2])
print overlap([4, 10, 2, 6, 3])
