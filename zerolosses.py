class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_wins = {}
        player_losses = {}
        
        # Count the wins and losses for each player
        for winner, loser in matches:
            player_wins[winner] = player_wins.get(winner, 0) + 1
            player_losses[loser] = player_losses.get(loser, 0) + 1
        
        # Find players who have not lost any matches
        not_lost = [player for player in player_wins if player not in player_losses]
        
        # Find players who have lost exactly one match
        lost_once = [player for player in player_losses if player_losses[player] == 1]
        
        # Sort the lists in increasing order
        not_lost.sort()
        lost_once.sort()
        
        return [not_lost, lost_once]