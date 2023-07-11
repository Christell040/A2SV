class Solution(object):
    def twoSum(self, numbers, target):
        
        "2 pointer approach"

        i = 0
        j = len(numbers)-1
        coordinates = []
        numbers = list(map(int,numbers))

        while i < j :
            if numbers[i] + numbers[j] > target:
                j-=1
            if numbers[i] + numbers[j] < target:
                i+=1
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]               
            
        