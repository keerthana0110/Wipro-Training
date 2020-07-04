# Python program to print odd Numbers in given range or print alternate numbers from 1 to 99

start, end = 1,100

# iterating each number in list 
for num in range(start, end + 1): 
	
	# checking condition 
	if num % 2 != 0: 
		print(num, end = " ") 
