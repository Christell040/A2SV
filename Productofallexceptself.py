class Solution(object):
    def productExceptSelf(self, nums):   
        n = len(nums)
        answer = [0] * n
        
        # Calculate the left products
        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Calculate the right products
        right_products = [1] * n
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        # Calculate the final answer
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]
        
        return answer
