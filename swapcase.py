def swap_case(text):
    swapped_text = ""
    for char in text:
        if char.islower():
            swapped_text += char.upper()
        elif char.isupper():
            swapped_text += char.lower()
        else:
            swapped_text += char
    return swapped_text

# Example usage

text = "Hello, World!"
result = swap_case(text)
print(result)  #
