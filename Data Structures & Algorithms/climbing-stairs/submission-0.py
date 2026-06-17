class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[None for i in range(n+1)]
        dp[0]=1
        dp[1]=1
        if n<=1:
            return 1
        dp[2]=2
        return self.calculateTimes(n,dp)

    def calculateTimes(self,n,dp)-> int:
        if dp[n]!=None:
            return dp[n]
        dp[n] = self.calculateTimes(n-1,dp) + self.calculateTimes(n-2,dp)
        return dp[n]