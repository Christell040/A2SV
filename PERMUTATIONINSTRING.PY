class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a  = len(s1)
        i = 0
        j = a
        
        while j<= len(s2):
            window = s2[i:j]
            content = Counter(window)       

            if window == s1 or content == Counter(s1):
                return True
            
            i+=1
            j+=1

        return False
