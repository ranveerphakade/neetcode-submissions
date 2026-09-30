class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        one =sorted(s)
        two = sorted(t)

        if one == two :
            return True 
        else:
            return False