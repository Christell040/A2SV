from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the lengths in descending order
        
        # Check all possible combinations of three lengths
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            
            if a < b + c:  # If the lengths can form a triangle
                return a + b + c  # Return the perimeter
        
        return 0  # No valid triangle found, return 0

# Create an instance of the Solution class
solution = Solution()

# Example usage
nums = [2, 1, 2]
result = solution.largestPerimeter(nums)
print("Input:", nums)
print("Output:", result)

nums = [1, 2, 1, 10]
result = solution.largestPerimeter(nums)
print("Input:", nums)
print("Output:", result)
