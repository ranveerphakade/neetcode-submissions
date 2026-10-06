class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        long = 0

        for num in nums :
            if (num -1 ) not in numset : 
                leg =0 
                while (num + leg) in numset :
                    leg +=1
                long = max(long, leg)
        return long