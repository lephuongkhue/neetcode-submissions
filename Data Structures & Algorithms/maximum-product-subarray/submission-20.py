# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         dp = [(1,1)] * len(nums)
#         dp1 = [(1,1)] * len(nums)
#         dp[0] = (nums[0], nums[0])
#         dp1[len(nums)-1] = (nums[len(nums)-1], nums[len(nums)-1])
#         for i in range(1,len(nums)):
#             if nums[i] > 0:
#             dp[i] = (max(nums[i] * dp[i-1], nums[i]), min(nums[i] * dp[i-1], nums[i]))
        
#         for i in range(len(nums)-2,-1,-1):
#             dp1[i] = (max(nums[i] * dp1[i+1], nums[i]), min(nums[i] * dp1[i+1], nums[i]))
            # print(i,'---')
            # print(dp1)

        # print(dp)
        # print(dp1)
        # return max(dp+nums+dp1)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         dp = [] *len(nums)
#         if len(nums)==1:
#             return nums[0]
#         for i in range(len(nums)):
#             # print(i,'----')
#             dp.append([nums[i]])
#             for j in range(i+1, len(nums)):
#                     dp[i].append(dp[i][-1] * nums[j])
#             # print(dp)
#         # print(dp)
#         # dp
#         return max(max(i) for i in dp)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(nums[i], currMax*nums[i])
            currMin = min(nums[i], currMin*nums[i])
            res = max(res, currMax)
        return res