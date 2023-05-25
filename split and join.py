def split_string(text):
    return text.split(" ")

# Example usage
text = "a string of space-separated words"
split_parts = split_string(text)
print(split_parts)  # Output: ['hello', 'world']


def join_parts(parts):
    return "-".join(parts)

# Example usage

joined_text = join_parts(split_parts)
print(joined_text)  # Output: "hello-world"
