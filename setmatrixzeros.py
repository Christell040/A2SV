class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows =set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)


        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        return matrix