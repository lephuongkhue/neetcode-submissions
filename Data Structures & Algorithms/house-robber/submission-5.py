class Solution:
        
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        return recurFunc(len(nums)-1, nums, dp)
        
def recurFunc(i:int, nums: List[int], dp: List[int]):
    if i < 2:
        return dp[i]
    if dp[i] == -1:
        dp[i] = max(recurFunc(i-1, nums, dp), recurFunc(i-2, nums, dp) + nums[i])
    return dp[i]
    