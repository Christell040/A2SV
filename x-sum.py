class Solution(object):
    def maxSum(self, grid):       
        rows = len(grid)
        cols = len(grid[0])
        max_sum = float('-inf')

        for i in range(rows - 2):  # Rows loop
            for j in range(cols - 2):  # Columns loop
                # Calculate the sum of the current hourglass
                current_sum = (
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                    grid[i + 1][j + 1] +
                    grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                )
                # Update the maximum sum if necessary
                max_sum = max(max_sum, current_sum)

        return max_sum
