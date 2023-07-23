class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

