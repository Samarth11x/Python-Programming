# Question 5: Reverse Words in a Sentence
# Input 'Python is fun' -> Output 'fun is Python'.

def reverse_word_order(sentence):
    """Reverses the order of words in a sentence."""
    
    # 1. Split the sentence into a list of words using whitespace as a delimiter
    words = sentence.split()
    
    # 2. Reverse the order of the words in the list
    # The [::-1] slice creates a reversed copy of the list
    reversed_words = words[::-1]
    
    # 3. Join the words back together into a single string, separated by a space
    reversed_sentence = " ".join(reversed_words)
    
    print("\n--- Word Reversal Result ---")
    print(f"Input Sentence: '{sentence}'")
    print(f"Output Sentence: '{reversed_sentence}'")
    print("----------------------------")
    
    return reversed_sentence

# Example Usage
reverse_word_order("Python is fun")

# Another example
reverse_word_order("The quick brown fox jumps")
