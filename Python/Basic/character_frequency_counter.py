from typing import Dict

# Question 3: Character Frequency Counter
# Input a string and display how many times each character occurs using a dictionary.


def count_char_frequency(input_string: str) -> Dict[str, int]:
    """Counts the frequency of each character in a string using a dictionary."""
    char_counts: Dict[str, int] = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    print("\n--- Character Frequency Analysis ---")
    print(f'Input String: "{input_string}"')
    print("\nFrequency Counts:")
    for char in sorted(char_counts):
        print(f"{repr(char)} : {char_counts[char]} time(s)")
    print("----------------------------------")
    return char_counts

if __name__ == "__main__":
    input_text_1 = "programming is fun"
    count_char_frequency(input_text_1)

    input_text_2 = "Hello World! 123"
    count_char_frequency(input_text_2)
