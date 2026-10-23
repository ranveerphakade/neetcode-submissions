class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r ,c =len(matrix), len(matrix[0])

        top , bot = 0 , r-1
        while top<= bot:
            rm =(top+bot)//2
            if target > matrix[rm][-1]:
                top = rm + 1
            elif target < matrix[rm][0]:
                bot = rm -1 
            else :
                break
            
        if not (top<=bot):
            return False
        
        l,r = 0, c-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[rm][m]:
                l = m+1
            elif target < matrix[rm][m]:
                r = m-1
            else :
                return True 
        return False