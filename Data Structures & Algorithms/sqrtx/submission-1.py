class Solution:
    def mySqrt(self, x: int) -> int:
        l , r = 0 , x
        res =0

        while l<=r :
            if m*m < res :
                r = m-1
            elif m*m > res:
                l= m+1
                res = m
            else :
                return m 
        return res 