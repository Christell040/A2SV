class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        def is_unidiagonal(row,col):
            val = matrix[row][col]

           

            while row < len(matrix) and col < len(matrix[0]):

                if matrix[row][col] != val:
                    return False
            
                row+=1
                col+=1

            return True

        for col in range(len(matrix[0])):
            
            if not is_unidiagonal(0,col):
                return False
            
            for row in range(1, len(matrix)):
                if not is_unidiagonal(row, 0):
                    return False
        return True
            
    
    'space complexity = O(1)'
    'time complexity = O(M * N)'