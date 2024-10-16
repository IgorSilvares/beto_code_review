"""
1. Given an array of strings, write a function which removes the duplicates.
For example, given the input = ["hello","hello", "world"], the output = ["hello", "world"]
"""

def remove_duplicates(array):
    unique = []
    for word in array:
        if word not in unique:
            unique.append(word)
    return unique


example = ["hello", "hello", "world"]
print(remove_duplicates(example))