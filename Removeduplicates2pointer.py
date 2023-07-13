class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            
            right += 1

        return left + 1