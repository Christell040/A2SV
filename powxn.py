# if n ==1:
        #     return x
        # elif n ==-1:
        #     return 1/x
        # elif n < 0 and n!= -1:
        #     return round((self.myPow(x,n+1) * 1/x),8)
        # else:
        #     return round((self.myPow(x,n-1) * x),8)

        def div(x,n):
            if x == 0 : return 0
            if n == 0 : return 1

            result = div(x,n//2)
            result*= result

            if n%2 != 0:
                return x* result
            else:
                return result
        
        return div(x,abs(n)) if n>= 0 else 1/div(x,abs(n))
