"""
Create a function named decode_garden_message that receives encoded_message and shift as its parameters.

This function decodes a message using a variation of the Caesar cipher, where each letter is shifted by a specified number of positions in the alphabet. Special characters ('!', '?', '.', ',', ':', ';') cause non-alphabetical characters to be reversed based on their position in the string.

Steps to solve:

Iterate through each character in encoded_message.
If the character is an alphabet (uppercase or lowercase), apply the Caesar cipher shift:
Convert the character to its ASCII code.
Subtract the ASCII code of 'A' (for uppercase) or 'a' (for lowercase) to get the zero-based index.
Apply the shift to the index, handling negative shifts and wrapping around the alphabet if necessary.
Convert the shifted index back to its corresponding ASCII code and then to the shifted character.
If the character is a special character, reverse the non-alphabetical characters encountered so far in the string.
If the character is neither an alphabet nor a special character, leave it unchanged.
Append the processed character to the decoded message string.
Return the decoded message string.

Parameters:

encoded_message (str): The encoded message string containing letters, numbers, and special characters.
shift (int): The number of positions each letter in the string will be shifted to decode the message. Positive values shift forward, negative values shift backward.
The function returns the decoded message as a string.
"""

def decode_garden_message(encoded_message, shift):
    special_chars = {'!', '?', '.', ',', ':', ';'}
    decoded_message = []
    non_alpha_chars = []

    for char in encoded_message:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            decoded_char = chr((ord(char) - base + shift) % 26 + base)
            decoded_message.append(decoded_char)
        elif char in special_chars:
            non_alpha_chars.reverse()
            decoded_message.extend(non_alpha_chars)
            non_alpha_chars = []
            decoded_message.append(char)
        else:
            non_alpha_chars.append(char)
    
    decoded_message.extend(non_alpha_chars)
    
    return ''.join(decoded_message)
