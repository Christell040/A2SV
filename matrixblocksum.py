class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        answer = [[0] * cols for _ in range(rows)]  # Initialize the answer matrix
        
        # Calculate the prefix sum of the matrix
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        
        # Calculate the sum for each element in the answer matrix
        for i in range(rows):
            for j in range(cols):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(rows - 1, i + k)
                c2 = min(cols - 1, j + k)
                answer[i][j] = prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]
        
        return answer

        'time complexity = O(m*n) space complexity = O(m*n)'