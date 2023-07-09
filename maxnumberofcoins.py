class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        piles.sort(reverse=True)  # Sort the piles in descending order
        n = len(piles)
        coins = 0
        i = 1  # Start from the second pile
        
        while i < n * 2 / 3:
            coins += piles[i]  # Add the coins from our chosen pile
            i += 2  # Move to the next pile with maximum coins
            
        return coins



     