class Solution(object):
    def matrixReshape(self, mat, r, c):
        original_rows = len(mat)
        original_cols = len(mat[0])
        
        if r * c != original_rows * original_cols:
            return mat
        
        flat_list = [element for row in mat for element in row]
        reshaped_matrix = [[0] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                reshaped_matrix[i][j] = flat_list[i * c + j]
        
        return reshaped_matrix