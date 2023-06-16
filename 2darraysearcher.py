class Solution(object):
    def searchMatrix(self, matrix, target):
       
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Start from the top-right corner of the matrix
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # Move down to the next row
                row += 1
            else:
                # Move left to the previous column
                col -= 1
        
        return False
