"""

Create a function named decode_cipher that receives text as its parameter.

This function decodes a ciphered string containing encoded messages about the history of Florence.

The ciphered string, text, contains 1 to 5 encoded sections marked by #start# and #end#. Each encoded section undergoes these transformations:

Extract the substring between the #start# and #end# markers. Reverse the extracted substring. 
Replace characters in the reversed substring using a substitution cipher (e.g., 'a' with 'z', 'b' with 'y').
Preserve characters without a mapping. Extract the first half of the transformed substring. 
After processing all encoded sections, concatenate the decoded substrings to form the final decoded message. Return this decoded message as a string.

Parameter:

text (str): The ciphered string containing encoded messages. 
It will contain 1 to 5 encoded sections marked by #start# and #end#. The substrings within the markers will be at most 100 characters long. The function returns the decoded message as a string, revealing the hidden information about Florence's history.

"""


def decode_cipher(text):
    import string
    
    # Create substitution cipher mapping (e.g., 'a' -> 'z', 'b' -> 'y')
    def substitution_cipher(char):
        if char.isalpha():
            if char.islower():
                return chr(219 - ord(char))  # 'a' (97) + 'z' (122) = 219
            elif char.isupper():
                return chr(155 - ord(char))  # 'A' (65) + 'Z' (90) = 155
        return char  # Preserve non-alphabetic characters

    decoded_message = ""
    start_marker = "#start#"
    end_marker = "#end#"
    start_index = 0

    while start_marker in text and end_marker in text:
        start_index = text.index(start_marker) + len(start_marker)
        end_index = text.index(end_marker)
        
        # Extract the substring between markers
        encoded_substring = text[start_index:end_index]
        
        # Reverse the extracted substring
        reversed_substring = encoded_substring[::-1]
        
        # Apply substitution cipher
        transformed_substring = ''.join(substitution_cipher(c) for c in reversed_substring)
        
        # Extract the first half of the transformed substring
        half_length = len(transformed_substring) // 2
        decoded_message += transformed_substring[:half_length]
        
        # Remove the processed section
        text = text[end_index + len(end_marker):]
    
    return decoded_message
