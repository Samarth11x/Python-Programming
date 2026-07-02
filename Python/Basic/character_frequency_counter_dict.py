# Question 3: Character Frequency Counter
# Input a string and display how many times each character occurs using a dictionary.

def count_char_frequency(input_string):
    """Counts the frequency of each character in a string using a dictionary."""
    
    # Dictionary to store character counts: {character: count}
    char_counts = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is already a key in the dictionary
        if char in char_counts:
            # If yes, increment its count
            char_counts[char] += 1
        else:
            # If no, add it to the dictionary with a count of 1
            char_counts[char] = 1
            
    print("\n--- Character Frequency Analysis ---")
    print(f"Input String: \"{input_string}\"")
    print("\nFrequency Counts:")
    
    # Print the results
    # We sort the keys to display them in a structured way
    for char, count in sorted(char_counts.items()):
        # Use repr() to correctly display whitespace characters like ' '
        print(f"{repr(char)} : {count} time(s)")
        
    print("----------------------------------")
    return char_counts

# Example Usage
input_text = "Organization is key for file management."
count_char_frequency(input_text)
