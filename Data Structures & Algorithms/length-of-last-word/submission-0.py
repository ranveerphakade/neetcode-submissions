class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leg = i =0
        while i < len(s):
            if s[i] == ' ' :
                while i < len(s) and s[i] ==' ':
                    i+=1
                if i == len(s):
                    return leg 
                leg =0 
            else :
                i+=1
                leg+=1
        return leg