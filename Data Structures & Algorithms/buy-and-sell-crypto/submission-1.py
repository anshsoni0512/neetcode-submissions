class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        maxprof=0
        for i in range(len(prices)): #buy

            for j in range(i+1,len(prices)): #sell

                profit=prices[j]-prices[i] #sell-buy
                maxprof=max(profit,maxprof) #compare current profit with previous profit
        return maxprof

        
        