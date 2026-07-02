# Python Basics - Beginner Friendly Notes + Examples
# Run this file and read the output section by section.
# Tip: Lines starting with # are comments. Python ignores them.

print("==============================")
print("1. PRINT STATEMENTS")
print("==============================")

print("Hello, world!")
print("My name is Samarth")
print("Python is fun!")

# You can print multiple things using commas.
print("Age:", 16)
print("Score:", 95, "out of", 100)

# \n means new line.
print("Line 1\nLine 2")


print("\n==============================")
print("2. VARIABLES")
print("==============================")

name = "Samarth"      # string / text
age = 16              # integer / whole number
height = 5.8          # float / decimal number
is_student = True     # boolean / True or False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Variables can be updated.
age = age + 1
print("Age next year:", age)


print("\n==============================")
print("3. DATA TYPES")
print("==============================")

text = "hello"
number = 10
decimal = 3.14
truth = False

print(type(text))
print(type(number))
print(type(decimal))
print(type(truth))


print("\n==============================")
print("4. BASIC MATH")
print("==============================")

a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     # normal division
print("a // b =", a // b)   # floor division
print("a % b =", a % b)     # remainder
print("a ** b =", a ** b)   # power


print("\n==============================")
print("5. STRINGS")
print("==============================")

first_name = "Samarth"
last_name = "Patil"
full_name = first_name + " " + last_name

print(full_name)
print(first_name.upper())
print(first_name.lower())
print("Length:", len(first_name))

# f-strings are a clean way to put variables inside text.
print(f"Hello, my name is {first_name} and I am {age} years old.")


print("\n==============================")
print("6. IF, ELIF, ELSE")
print("==============================")

marks = 82

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Important comparison operators:
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print("\n==============================")
print("7. LOGICAL OPERATORS")
print("==============================")

age = 18
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")

weather = "rainy"

if weather == "sunny" or weather == "cloudy":
    print("Good day to go outside")
else:
    print("Maybe stay inside")

is_tired = False

if not is_tired:
    print("Ready to study")


print("\n==============================")
print("8. FOR LOOPS")
print("==============================")

# range(5) gives 0, 1, 2, 3, 4
for i in range(5):
    print("i =", i)

# range(start, stop) stops before the stop number.
for num in range(1, 6):
    print("Number:", num)

# Loop through a string.
for letter in "Python":
    print(letter)


print("\n==============================")
print("9. WHILE LOOPS")
print("==============================")

count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1


print("\n==============================")
print("10. BREAK AND CONTINUE")
print("==============================")

for num in range(1, 10):
    if num == 5:
        break  # stops the loop completely
    print("Before break:", num)

for num in range(1, 6):
    if num == 3:
        continue  # skips this round only
    print("Using continue:", num)


print("\n==============================")
print("11. LISTS")
print("==============================")

fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])      # first item
print(fruits[-1])     # last item

fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

for fruit in fruits:
    print("Fruit:", fruit)


print("\n==============================")
print("12. TUPLES")
print("==============================")

# Tuples are like lists, but you usually do not change them.
coordinates = (10, 20)
print(coordinates)
print("x:", coordinates[0])
print("y:", coordinates[1])


print("\n==============================")
print("13. DICTIONARIES")
print("==============================")

student = {
    "name": "Samarth",
    "age": 16,
    "grade": "A"
}

print(student)
print(student["name"])
print(student["age"])

student["age"] = 17
student["city"] = "Delhi"
print("Updated student:", student)

for key, value in student.items():
    print(key, "=", value)


print("\n==============================")
print("14. FUNCTIONS")
print("==============================")

# A function is a reusable block of code.
def greet():
    print("Hello from a function!")

greet()
greet()

# Function with parameter.
def greet_person(person_name):
    print("Hello", person_name)

greet_person("Samarth")
greet_person("Python learner")

# Function that returns a value.
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 7)
print("Sum:", result)


def is_even(num):
    return num % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


print("\n==============================")
print("15. INPUT")
print("==============================")

# Uncomment these lines when you want to practice input.
# user_name = input("Enter your name: ")
# print("Hello", user_name)

# input() always gives text, so convert it for math.
# user_age = int(input("Enter your age: "))
# print("Next year you will be", user_age + 1)


print("\n==============================")
print("16. TRY / EXCEPT")
print("==============================")

# try/except helps handle errors without crashing your program.
try:
    answer = 10 / 2
    print("Answer:", answer)
except ZeroDivisionError:
    print("You cannot divide by zero")

try:
    number_text = "123"
    converted_number = int(number_text)
    print("Converted:", converted_number)
except ValueError:
    print("That text cannot be converted to a number")


print("\n==============================")
print("17. SIMPLE MINI PROGRAMS")
print("==============================")

# Mini Program 1: Check voting age.
person_age = 18

if person_age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# Mini Program 2: Find the largest number.
x = 12
y = 25
z = 9

if x >= y and x >= z:
    print("Largest is", x)
elif y >= x and y >= z:
    print("Largest is", y)
else:
    print("Largest is", z)

# Mini Program 3: Print multiplication table.
table_number = 5

for i in range(1, 11):
    print(table_number, "x", i, "=", table_number * i)


print("\n==============================")
print("18. PRACTICE QUESTIONS")
print("==============================")

print("1. Make a program that checks if a number is positive, negative, or zero.")
print("2. Make a function that returns the square of a number.")
print("3. Print all even numbers from 1 to 50.")
print("4. Make a list of 5 names and print each name.")
print("5. Make a calculator using functions: add, subtract, multiply, divide.")

print("\nYou finished the Python basics file. Keep cooking, bro.")
