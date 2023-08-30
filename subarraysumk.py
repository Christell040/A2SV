
# nums = [1,2,3,4,5]

# def is_divisible_k(num):
#         if num % 2 == 0:
#             return True
#         return False
    
# d_a = [i for i in nums if is_divisible_k(i)]
# print(d_a)

# def runningSum(nums):
#     p_sum = [0]*len(nums)

#     for i in range(len(nums)):
#         if i == 0:
#             p_sum[i] = nums[i]
        
#         p_sum[i]= nums[i]+p_sum[i-1]
#     return p_sum

# nums = [4,5,0,-2,-3,1]
# print(runningSum(nums))

class Solution(object):
    def subarraySum(self, nums, k):
        p_sum = [0]*len(nums)   

        for i in range(len(nums)):
            if i == 0:
                p_sum[i] = nums[i]
            else:            
                p_sum[i]= nums[i]+p_sum[i-1]
        
        count = 0

        dict_count = {0:1}

        for sum in p_sum:
            complement = sum-k

            if complement in dict_count:
                count += dict_count[complement]
            
            if sum in dict_count:
                dict_count[sum] +=1
            else:
                dict_count[sum]= 1
        return count   

