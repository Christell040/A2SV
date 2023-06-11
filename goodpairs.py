class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       
        count = 0  
        freq = {}  
        
        r
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        
        for num in freq:
            count += (freq[num] * (freq[num] - 1)) // 2
        
        return count
