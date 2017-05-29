#Write a function called lucky_sevens which takes an array of integers 
#and returns true if any three consecutive elements sum to 7.



def sevens(arr):

	consec_sevens = "false"
	sum=0
	for i in range(2,len(arr)):
		sum = arr[i-2]+arr[i-1]+arr[i]
		if sum == 7:
			 consec_sevens = "true"



	return consec_sevens

print sevens([3,54,6,8,4,3,0,5,67,8,5,43,3,5,67,5])     #true
print sevens([3,54,6,8,4,3,5,67,8,5,43,3,5,67,5])       #false
print sevens([3,54,6,8,4,3,0,5,67,8,5,43,3,5,67,5,1,1]) #true
print sevens([2,3,2,54,6,8,4,3,0,5,67,8,5,43,3,5,67,5]) #true











