class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min=prices[0]
        for i in range(len(prices)):
            temp=prices[i]-min
            if(temp>max_profit):
                max_profit=temp
            if prices[i]<min:
                min=prices[i]

        return max_profit