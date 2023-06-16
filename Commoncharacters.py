from collections import Counter

class Solution(object):
    def commonChars(self, words):        


        char_count = Counter(words[0])  # Initialize with the first word

        for word in words[1:]:
            word_count = Counter(word)
            for char in char_count:
                char_count[char] = min(char_count[char], word_count[char])  

        result = []
        for char, count in char_count.items():
            result.extend([char] * count)  

        return result