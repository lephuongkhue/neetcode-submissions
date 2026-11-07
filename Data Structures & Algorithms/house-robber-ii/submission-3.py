class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        # nums.append(min(nums[0], nums[-1]))
        size = len(nums)-1
        dp_skip_1 = [-1]*size
        dp_skip_last = [-1]*size
        dp_skip_1[0] = nums[1]
        dp_skip_last[0] = nums[0]
        dp_skip_last[1] = max(nums[0],nums[1])
        dp_skip_1[1] = max(nums[1],nums[2])
        for i in range(1,len(nums)):
            if dp_skip_1[i-1] == -1:
                dp_skip_1[i-1] = max(dp_skip_1[i-2], dp_skip_1[i-3] + nums[i])

        for i in range(size):
            if dp_skip_last[i] == -1:
                dp_skip_last[i] = max(dp_skip_last[i-1], dp_skip_last[i-2] + nums[i])
        

        return max(dp_skip_last[len(nums)-2], dp_skip_1[len(nums)-2]) 