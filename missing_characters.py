import string

def missingCharacters(user_string):
    alphabet = set(string.ascii_lowercase)
    odd_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    input_chars = set(user_string.lower())
    missing_alphabet = alphabet - input_chars
    missing_digits = odd_digits - input_chars
    missing_chars = sorted(missing_alphabet | missing_digits)
    return ''.join(missing_chars)
    
    
s = input()
print(missingCharacters(s))