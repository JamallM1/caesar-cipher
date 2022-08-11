import re
import string

def encrypt(code, key):
    punctuation = list(string.punctuation)
    encryptions = []

    for char in code:
        if char.isspace():
            encryptions.append(char)
        if char.isdigit():
            encryptions.append(char)
        if char in punctuation:
            encryptions.append(char)
        if char.isalpha():
            cipher = ""
            stationary_alpha = ord(char) + key

        if stationary_alpha > ord ('z'):
            stationary_alpha <= 26
