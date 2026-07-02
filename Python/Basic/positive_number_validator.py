# Question 6: Raise ValueError for Negative Input

def process_positive_number(number):
    """
    Checks if a number is positive. Raises ValueError if it is negative.
    
    Args:
        number (int or float): The input value.
    Returns:
        str: A message indicating the number is valid.
    Raises:
        ValueError: If the input number is less than zero.
    """
    if number < 0:
        raise ValueError(f"Input number cannot be negative. Received: {number}")
    
    # If the number is zero or positive, proceed
    return f"Success: The number {number} is valid."

# Example Usage 1: Valid input
print("--- Test 1 (Valid) ---")
print(process_positive_number(15))

# Example Usage 2: Invalid input (demonstrating the ValueError)
# We use a try/except block to catch the deliberate error and continue execution
print("\n--- Test 2 (Invalid) ---")
try:
    process_positive_number(-5)
except ValueError as e:
    print(f"Caught expected error: {e}")
