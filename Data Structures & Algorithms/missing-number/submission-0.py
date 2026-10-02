class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set(nums)
        n=len(nums)
        for i in range (n+1) :
            if i not in num :
                return i
        return 0
