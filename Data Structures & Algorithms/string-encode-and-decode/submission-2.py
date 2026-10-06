class Solution:

    def encode(self, strs: List[str]) -> str:
        rs=[]
        for s in strs:
            rs.append(str(len(s)))
            rs.append('#')
            rs.append(s)
        return "".join(rs)

    def decode(self, s: str) -> List[str]:
        rs=[]
        i=0
        while i <len(s):
            j =i
            while s[j] != '#':
                j+=1
            leg = int(s[i:j])
            i = 1 + j
            j = i + leg 
            rs.append(s[i:j])
            i =j 

        return rs
