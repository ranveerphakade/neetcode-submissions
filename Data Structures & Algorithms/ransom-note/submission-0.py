class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countr= Counter(ransomNote)
        countm = Counter(magazine)

        for i in countr:
            if countm[i]<countr[i]:
                return False
        return True