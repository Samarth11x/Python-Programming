# Question 1: String Analyzer
# Takes a sentence as input and prints the number of vowels, consonants, words,
# and uppercase/lowercase letters.

def analyze_sentence(sentence):
    """Analyzes a sentence and returns counts of various character types."""
    
    # Standard sets for comparison
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through the sentence character by character
    for char in sentence:
        if 'A' <= char <= 'Z':
            uppercase_count += 1
        elif 'a' <= char <= 'z':
            lowercase_count += 1

        # Check for vowels and consonants (case-insensitive)
        lower_char = char.lower()
        if lower_char in vowels:
            vowel_count += 1
        elif lower_char in consonants:
            consonant_count += 1
            
    # Count words by splitting the string by whitespace
    words = list(filter(None, sentence.split()))
    word_count = len(words)
    
    print("\n--- Analysis Results ---")
    print(f"Input Sentence: \"{sentence}\"")
    print(f"Number of Vowels: {vowel_count}")
    print(f"Number of Consonants: {consonant_count}")
    print(f"Number of Words: {word_count}")
    print(f"Number of Uppercase Letters: {uppercase_count}")
    print(f"Number of Lowercase Letters: {lowercase_count}")
    print("------------------------")

# Example Usage
input_sentence = "The Quick Brown Fox Jumps Over The Lazy Dog. 123"
analyze_sentence(input_sentence)

# Another example with mixed spacing/punctuation
analyze_sentence("Hello World! It's Fun.")