# Asking user to input five integers
input_values = input("Enter five integers separated by commas (e.g., 35,55,75,25,65): ")
numbers = [int(x.strip()) for x in input_values.split(",")]

# Creating list and tuple
num_list = numbers
num_tuple = tuple(numbers)

# Finding largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Displaying results
print("List:", num_list)
print("Tuple:", num_tuple)
print("Largest number:", largest)
print("Smallest number:", smallest)
