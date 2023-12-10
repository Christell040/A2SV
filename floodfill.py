class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #this method will use matrix dfs

        def dfs(image, row, col, original_color, new_color):
            if (
                row < 0 or row >= len(image) or
                col < 0 or col >= len(image[0]) or
                image[row][col] != original_color
            ):
                return
            
            image[row][col] = new_color

            # Explore 4-directionally connected pixels
            dfs(image, row + 1, col, original_color, new_color)  # Down
            dfs(image, row - 1, col, original_color, new_color)  # Up
            dfs(image, row, col + 1, original_color, new_color)  # Right
            dfs(image, row, col - 1, original_color, new_color)  # Left


        if not image or image[sr][sc] == color:
            return image
    
        original_color = image[sr][sc]
        dfs(image, sr, sc, original_color, color)
        return image
