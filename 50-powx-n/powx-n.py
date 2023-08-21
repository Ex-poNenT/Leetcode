class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
            return 1
        def helper(x,n) :
            if n == 1 :
                return x 
            return helper(x*x,n//2) if n%2 == 0 else x*helper(x*x,n//2)
        if n>0 :
            return helper(x,n)
        return 1/helper(x,-n)
            
