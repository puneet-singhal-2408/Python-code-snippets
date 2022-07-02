print("Enter the first value") # when this is included in input operator program is showing error
x = int(input()) # user input is converted into integer value 
print("choose the an operation :" "+", "-", "*", "/","%") # required operator is defined as string
y = input() # this variable will have user input as string 
print("Enter the second value")
z = int(input()) # user input is converted into integer value 
if y== "+":  # perform addition
	print(x + z)
elif y == "-": # perform subtraction
    print(x - z)
elif y == "*": # perform multiplication
    print(x * z)
elif y== "/": # perform division
    print(x / z)
elif y== "%": # perform percentage
    print((x * z) / 100 )
else: # if nothing goes well 
	print("something is wrong")
