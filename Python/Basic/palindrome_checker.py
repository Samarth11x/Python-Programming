# Program to check if a string is a palindrome

text = input("Enter a string: ")

# Check if the string is equal to its reverse
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
