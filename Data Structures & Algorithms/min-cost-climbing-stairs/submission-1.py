class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0]*(length+1)
        if length == 1:
            return cost[0]
        elif length == 2:
            return min(cost[0], cost[1])
        
        dp[0] = 0
        # dp[2] = min(cost[0], cost[1]) + cost[2]
        dp[1] = 0
        for i in range(2,length+1):
            print(dp)
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]