class Solution(object):
    def lengthOfLongestSubstring(self, s):
        characters = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l +=1
            characters.add(s[r])
            result = max(result,r-l+1)
        return result
