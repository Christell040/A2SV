class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        less = []
        

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    count +=1
            less.append(count)
        
        return less

        'space complexity = 0(n)'
        'time complexity = O(n^2) '