class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def power(n):
            
            
            if n==1:
                return x
            if n==0:
                return 1

            
            res = power(n-(n//2)) * power(n//2)
                
            return res
        return power(n) if n>=0 else 1/power(abs(n))
            

        