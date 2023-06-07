class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1
        
        for i, point in enumerate(points):
            px, py = point[0], point[1]
            
            if px == x or py == y:  # Check if the point is valid
                distance = abs(px - x) + abs(py - y)
                
                if distance < min_distance:
                    min_distance = distance
                    min_index = i
        
        return min_index


