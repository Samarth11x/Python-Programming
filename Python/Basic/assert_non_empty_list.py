# Question 8: Assertion to Ensure List is Not Empty

def process_data_list(data_list):
    """
    Processes a list only if it is not empty, using an assertion.
    
    Args:
        data_list (list): The list of data to process.
    """
    
    # The 'assert' statement checks a condition. If the condition is False, 
    # it raises an AssertionError with the optional message.
    assert len(data_list) > 0, "List must not be empty for processing."
    
    # If the assertion passes, the program continues
    total = sum(data_list)
    average = total / len(data_list)
    
    print(f"List successfully processed: {data_list}")
    print(f"Total Sum: {total}")
    print(f"Average: {average}")


# Example Usage 1: Valid non-empty list
print("--- Test 1 (Valid List) ---")
process_data_list([10, 20, 30, 40])

# Example Usage 2: Invalid empty list (demonstrating the AssertionError)
# Assertions are often disabled in production, but are good for debugging/testing.
print("\n--- Test 2 (Empty List) ---")
try:
    process_data_list([])
except AssertionError as e:
    print(f"Caught expected error: {e}")
