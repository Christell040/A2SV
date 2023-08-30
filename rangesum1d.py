class NumArray(object):

    def __init__(self, nums):
        self.p_sum=[0]*len(nums)

        for i in range(len(nums)):                     
            if i == 0:
                self.p_sum[i] = nums[i]
            else:
                self.p_sum[i] = nums[i]+self.p_sum[i-1]
        
        

    def sumRange(self, left, right):
        if left == 0:
            return self.p_sum[right]

        return self.p_sum[right]-self.p_sum[left-1]

       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)