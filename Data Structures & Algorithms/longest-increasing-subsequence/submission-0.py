class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        dp[len(nums)-1] = 1
        for i in range(len(nums)-1, -1,-1):
            # print(i,'----')
            pre = nums[i]
            currLen = 1
            for j in range(i, len(nums)):
                # print(j)
                # print(nums[i])
                # print(nums[j])
                if nums[i] < nums[j]:
                    currLen = max(currLen, 1 + dp[j])
                    # print('valid', currLen)
            dp[i] = currLen
        print(dp)
        return max(dp)
            # current = nums[i]
            # for j in range(i, len(nums)):
            #     if nums[i]