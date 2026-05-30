class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        for i in range(len(prices)):

            for j in range(i+1,len(prices)):

                profit=prices[j]-prices[i]
                maxprof=max(profit,maxprof)
        return maxprof
        