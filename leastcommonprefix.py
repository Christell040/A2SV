def find_least_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]  # Initialize prefix with the first string
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character from prefix
            if not prefix:
                return ""  # No common prefix found

    return prefix

# Example usage
arr = ["apple", "ape", "app", "april"]
result = find_least_common_prefix(arr)
print("Least common prefix:", result)