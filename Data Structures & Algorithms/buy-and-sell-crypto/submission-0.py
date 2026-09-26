class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        mp=0

        while r<len(prices):
            if prices[l] < prices[r]:
                p = prices[r]-prices[l]
                mp = max(mp,p)
            else :
                l+=1
            r+=1
        return mp