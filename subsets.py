class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def distinct(nums):
            subs = []
            current = []
            
            solve(0,nums,current,subs)
            return subs

        def solve(i,nums,current,subs):
            if i >= len(nums):
                subs.append(current.copy())
                return

            current.append(nums[i])
            solve(i+1,nums,current,subs)
            current.pop()

            solve(i+1,nums,current,subs)
        
        return distinct(nums)
