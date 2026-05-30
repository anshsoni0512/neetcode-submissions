class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # maxprof=0
        # for i in range(len(prices)): #buy

        #     for j in range(i+1,len(prices)): #sell

        #         profit=prices[j]-prices[i] #sell-buy
        #         maxprof=max(profit,maxprof) #compare current profit with previous profit
        # return maxprof


        #Optimal Solution ---> O(n)
        l = 0
        r = 1
        maxProf = 0
        while r<len(prices):
            
            if prices[l]<prices[r]: # we are in profit
                profit = prices[r] - prices[l]
                maxProf = max(profit,maxProf)
            else:    # we are in loss
                l = r
            r = r+1
        return maxProf
        
               


        
        