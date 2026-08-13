class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if  prices[j]-prices[i]>profit:
                    profit=prices[j]-prices[i] 
        return profit


#time complexity o(n^2) :: Bruteforce method
#By ::Prabesh Amgain
#Timeframe :: 2026-08-13