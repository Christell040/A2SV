class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n-1):
                for j in range(n-1-i):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]

            return arr
        
        return bubble_sort(nums)