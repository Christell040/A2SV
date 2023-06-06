class Solution:
    def isAlienSorted(self, words, order):
        order_dict = {c: i for i, c in enumerate(order)}
        
        for i in range(1, len(words)):
            if not self.compare_words(words[i-1], words[i], order_dict):
                return False
        return True
    
    def compare_words(self, word1, word2, order_dict):
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                if order_dict[char1] > order_dict[char2]:
                    return False
                else:
                    return True
        return len(word1) <= len(word2)