# Original list
numbers = [10, 30, 20, 60, 80, 20, 40, 60, 20]

# Finding index positions of element 20
indices = [i for i, val in enumerate(numbers) if val == 20]
print("Index positions of 20:", indices)

# Removing all occurrences of 20
filtered_list = [val for val in numbers if val != 20]
print("List after removing 20:", filtered_list)
