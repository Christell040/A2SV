class Solution(object):
    def runningSum(self, nums):
        p_sum = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
               p_sum[i] = nums[i]
            
            p_sum[i]= nums[i]+p_sum[i-1]
        return p_sum
