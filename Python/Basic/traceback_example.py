# Question 7: Traceback Module
import traceback

def function_a():
    """This function intentionally causes a division by zero error."""
    # This will cause ZeroDivisionError
    result = 10 / 0 
    return result

def function_b():
    """Calls function_a, creating a nested call stack."""
    print("Function B is running...")
    return function_a()

def main_program():
    """The main entry point where the error is caught and printed."""
    print("Starting main program.")
    try:
        function_b()
    except Exception:
        # Instead of just printing the error message, we print the full traceback
        print("\n--- Full Traceback Output ---")
        # traceback.print_exc() prints the traceback directly to the console
        traceback.print_exc(limit=None) 
        print("-----------------------------")
    print("Program execution finished after printing traceback.")

# Execute the program
main_program()
