# Question 2: Title Formatter
# Takes a paragraph and capitalizes the first letter of every sentence.
import re

def capitalize_sentences(paragraph):
    """Capitalizes the first letter of every sentence in a given paragraph."""
    
    # Ensure the paragraph is treated as a string
    if not isinstance(paragraph, str):
        return ""
    
    # 1. Strip leading/trailing whitespace
    paragraph = paragraph.strip()
    if not paragraph:
        return ""

    # 2. Capitalize the very first letter of the paragraph
    if paragraph[0].isalpha():
        paragraph = paragraph[0].upper() + paragraph[1:]
    
    # 3. Use regex to find punctuation (. ! ?) followed by whitespace and a letter.
    # Pattern: (End-of-sentence punctuation) + (zero/more whitespace) + (one lowercase letter)
    capitalized_paragraph = re.sub(r'([.!?])(\s*)([a-z])', 
                                  lambda m: m.group(1) + m.group(2) + m.group(3).upper(), 
                                  paragraph)
    
    print("\n--- Title Formatter Result ---")
    print(f"Original Paragraph:\n{paragraph}")
    print(f"\nFormatted Paragraph:\n{capitalized_paragraph}")
    print("------------------------------")
    return capitalized_paragraph

# Example Usage
text = "python is a versatile language. it is used for web development, data analysis, and machine learning! how fascinating is that? i love it."
capitalize_sentences(text)
