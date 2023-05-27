def merge_strings(word1, word2):
    merged = ''
    length = min(len(word1), len(word2))

    
    for i in range(length):
        merged += word1[i] + word2[i]

   
    if len(word1) > length:
        merged += word1[length:]
    elif len(word2) > length:
        merged += word2[length:]

    return merged


# Test the function
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
result = merge_strings(word1, word2)
print(result)
