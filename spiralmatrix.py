class Solution(object):
    def spiralOrder(self, matrix):
        "time complexity : O(mxn) space complexity O(1)"
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        res = []
        
        while left < right and top < bottom:
		
		'collect items from left to right and increase top pointer'
            for col in range(left,right):
                res.append(matrix[top][col])
            top += 1
		'collect items from top to bottom and reduce right pointer'
            for col in range(top,bottom):
                res.append(matrix[col][right-1])
            right -= 1
		
		"check if theres still more room for operation"
            if not(left < right and top < bottom):
                break
		
		"collect from right to left in a reverse fashion"
            for col in range(right - 1,left - 1 ,-1) :
                res.append(matrix[bottom-1][col])
            bottom -= 1 
		
		"take from bottom to top"
            for row in range(bottom-1,top-1,-1):
               res.append(matrix[row][left])
            left+=1
        
        return res