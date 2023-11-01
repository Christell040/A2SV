class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Using character frequencies

        counter = {}
        result = 0

        left = 0

        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right],0)

            #right - left + 1 = lenght of window

            while (right -left+1) - max(counter.values()) > k:
                counter[s[left]] -=1
                left+=1
            
            result = max(result, (right-left+1))
        return result
