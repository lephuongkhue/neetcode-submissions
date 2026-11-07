class Solution:
    def numDecodings(self, s: str) -> int:
        # def letterToNumber:
            # return ord('A') - ord('A') + 1
        # res = 0
        dp = [0]*len(s)
        length = len(s)

        if s[0] == '0':
            return 0
        
        if length == 1:
            return 1

        dp[0] = 1

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or int(s[i-1] + s[i]) > 26:
                    return 0
                else:
                    if i == 1: dp[1] = 1
                    else: dp[i] = dp[i-2]
            elif int(s[i-1] + s[i]) > 26 or s[i-1] == '0':
                dp[i] = dp[i-1]
            else: 
                if i == 1:
                    dp[i] = 2
                else: dp[i] = dp[i-1]+ dp[i-2]
                print(dp)
        return dp[-1]