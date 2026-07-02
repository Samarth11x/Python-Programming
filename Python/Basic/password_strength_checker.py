# Question 4: Password Strength Checker
# Checks if a password is strong (at least 8 chars, 1 uppercase, 1 lowercase, 
# 1 digit, 1 special character).

def check_password_strength(password):
    """Checks a password against five strength criteria."""
    
    # Criteria flags
    min_length = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Define special characters (anything that is not alphanumeric or whitespace)
    special_chars = "!@#$%^&*()-_+=[]{}|\\:;\"'<>,.?/~`"
    
    # Iterate through the password once to check all character-based criteria
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    # Compile the results
    is_strong = all([min_length, has_upper, has_lower, has_digit, has_special])
    
    print("\n--- Password Strength Report ---")
    print(f"Password: {password}")
    print(f"Is Strong: {is_strong}")
    
    # Detailed breakdown of criteria
    print("\nCriteria Check:")
    print(f"- Minimum 8 characters: {min_length}")
    print(f"- Contains uppercase letter: {has_upper}")
    print(f"- Contains lowercase letter: {has_lower}")
    print(f"- Contains a digit: {has_digit}")
    print(f"- Contains a special character: {has_special}")
    print("--------------------------------")
    
    return is_strong

# Example Usage
check_password_strength("P@sswOrd123")

# Example 2: Weak Password (missing special char)
check_password_strength("PythonFun1")

# Example 3: Weak Password (too short)
check_password_strength("Short1")
