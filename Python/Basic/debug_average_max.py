# Question 10: Debugging Practice (Logic Error)

def calculate_average_and_find_max(numbers):
    """
    Calculates the average of a list of integers and finds the maximum value.
    
    NOTE: This function contains an intentional LOGIC ERROR (not a crash) that 
    a debugger would help find. The total sum is calculated incorrectly.
    """
    
    # INTENTIONAL BUG 1: Logic error in calculating the sum
    # The loop below will FAIL TO ADD the first element (numbers[0]) to the total.
    # The loop should start at index 0, but currently starts at index 1.
    
    total = 0
    
    # Bug starts here: Range starts at 1, skipping numbers[0]
    for i in range(1, len(numbers)): 
        total += numbers[i]
        
    # The max function is correct
    max_value = max(numbers)
    
    # The average calculation is correct based on the *flawed* total
    # This assumes the list is not empty
    avg = total / len(numbers)
    
    print("\n--- Debugging Practice Results ---")
    print(f"Input list: {numbers}")
    print(f"Expected Sum (Correct): {sum(numbers)}")
    print(f"Actual Calculated Sum (BUG): {total}") # This line reveals the bug
    print(f"Calculated Average: {avg}")
    print(f"Max Value: {max_value}")
    print("\n--- Debugger Analysis ---")
    print("To find the error, one would use IDLE's Debugger (or VS Code/Jupyter):")
    print("1. Set a breakpoint on the line: 'total = 0'")
    print("2. Step through the 'for' loop using 'Step Over' or 'Step Into'.")
    print("3. Observe the 'Variables' window as the loop executes.")
    print("4. Notice that when the loop starts, 'i' is 1, and 'total' skips the value of numbers[0].")
    print("5. FIX: Change 'range(1, len(numbers))' to 'range(len(numbers))' or simply 'for num in numbers:'.")
    print("----------------------------------")
    
    return avg, max_value

# Example Usage
sample_data = [10, 20, 30, 40]
calculate_average_and_find_max(sample_data)
