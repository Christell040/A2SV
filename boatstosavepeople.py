class Solution(object):
    def numRescueBoats(self, people, limit):
        
        people.sort()  # Sort the people array in non-decreasing order
        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats

    
                    





