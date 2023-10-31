class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def is_odd(num):
            if num %2 == 0:
                return False
            return True
       
        nice = 0
        count = 0
        odd= 0
        l = 0

        for num in nums:
            if is_odd(num):
                odd += 1
                count = 0

                while odd == k:
                    if  is_odd(nums[l]):
                        odd -= 1
                    l += 1
                    count += 1
            nice += count

        return nice
   
