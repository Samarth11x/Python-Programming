# Question 9: Logging all User Actions and Errors
import logging
import os

LOG_FILE = "program_activity.log"

# 1. SETUP: Remove previous log file for a clean run
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

# 2. SOLUTION: Set up logging configuration
# Configure the logging system to write to a file and include timestamps
logging.basicConfig(
    level=logging.INFO, # Set base level to INFO (includes INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_FILE,
    filemode='w' # 'w' overwrites the file each time
)

def perform_operation(x, y):
    """Simulates a user operation and logs the activity/errors."""
    logging.info(f"User Action: Attempting operation on {x} and {y}")
    
    try:
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        result = x / y
        logging.info(f"Operation Success: Result is {result}")
        return result
        
    except ZeroDivisionError as e:
        logging.error(f"Operation Failed: {e}")
        return None
    except Exception as e:
        logging.critical(f"Unexpected Error: {e}")
        return None

# Execute Operations
perform_operation(100, 5) # Success (INFO logged)
perform_operation(50, 0) # Failure (ERROR logged)
perform_operation(25, 2) # Success (INFO logged)

print(f"Log file '{LOG_FILE}' created successfully.")
print("--- Log File Content ---")
# Read and print the content of the log file to the console
with open(LOG_FILE, 'r') as f:
    print(f.read().strip())
print("------------------------")
