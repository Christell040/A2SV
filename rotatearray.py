class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        n = len(nums)

        nums[n-k:],nums[:n-k] = nums[:n-k],nums[n-k:]

        return nums
    