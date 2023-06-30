class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """  
        n = len(names)
       
        people = [(names[i], heights[i]) for i in range(n)]        
        
        people.sort(key=lambda x: x[1], reverse=True)        
        
        sorted_names = [person[0] for person in people]
        
        return sorted_names