class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)

        count = 0
        x = 0

        for num in flowerbed:
            if num == 0:
                count+=1
                if count == 3:
                    x+=1
                    count = 1
            elif num == 1:
                count = 0
        
        if n > x:
            return False
        return True

