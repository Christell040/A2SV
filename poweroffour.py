if n == 1:
            return True
        if n < 1:
            return False    
        return self.isPowerOfFour(n/4)
