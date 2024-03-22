class Solution:
    def getPermutation(self, n: int, k: int) -> str:       
        
        def helper(i):   
            if i == n+1:
                return [[]]
            
            resPerms = []
            perms = helper(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, i)
                    resPerms.append(pCopy)
            return resPerms

    
        res = helper(1)
        res.sort()
        a = "".join(map(str,res[k-1]))        
        return a
