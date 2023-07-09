class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        nums = list(map(str,nums))

        def compare(x,y):
            if x+y > y+x :
                return -1
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(compare)) #compare function imported from functools'

        return str(int("".join(nums)))

        'time complexity  = O(nlogn) space = O(n)'