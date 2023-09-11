class Solution(object):
    def isValid(self, s):  
        mapping = {")":"(" ,"]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        
