# Creating a dictionary of student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88
}

# Printing all keys
print("Student Names:", student_marks.keys())

# Printing all values
print("Marks:", student_marks.values())

# Printing key-value pairs
print("Student Marks:")
for name, marks in student_marks.items():
    print(name, ":", marks)
