class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0  
       
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                
                if self.isSimilar(words[i], words[j]):
                    count += 1
        
        return count
    
    def isSimilar(self, word1, word2):
        
        chars1 = set(word1)
        chars2 = set(word2)

        if chars1 == chars2:
            return True
        else:
            return False