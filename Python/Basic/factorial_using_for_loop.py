# Function to calculate factorial using for loop

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
