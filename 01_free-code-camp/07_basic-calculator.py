number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
result = number1 + number2

# string output
print("String: " + result) 

# decimal output
result = float(number1) + float(number2)
print("Float: " + str(result)) 
print(result)

# integer output
result = int(number1) + int(number2) # doesn't support decimal
print("Integer: " + str(result) )
print(result)