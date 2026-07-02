#Program to perform basic arithmetic operations on two integers

# Taking input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Performing operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handling division safely
if num2 != 0:
    quot_result = num1 / num2
    rem_result = num1 % num2
else:
    quot_result = "Undefined (division by zero)"
    rem_result = "Undefined (modulo by zero)"

# Displaying results
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quot_result}")
print(f"Remainder: {rem_result}")
