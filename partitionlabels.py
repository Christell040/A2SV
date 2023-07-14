class Solution(object):
    def partitionLabels(self, s):
        
        last_index = {}

        for i,c in enumerate(s):
            last_index[c] = i
        
        result = []
        size,end = 0,0

        for i,c in enumerate(s):
            size +=1
            end = max(end, last_index[c])

            if i == end:
                result.append(size)
                size = 0
        return result