#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]

# Test cases
print(remove_char_at("Best School", 3))  # Output: Bes School
print(remove_char_at("Chicago", 2))      # Output: Chcago
print(remove_char_at("C is fun!", 0))    # Output:  is fun!
print(remove_char_at("School", 10))      # Output: School
print(remove_char_at("Python", -2))     # Output: Python
