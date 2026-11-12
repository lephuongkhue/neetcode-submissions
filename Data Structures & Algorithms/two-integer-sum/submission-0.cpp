class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> idxMapper;
        vector<int> res;

        for (int i=0; i<nums.size(); i++)
        {
            int diff = target - nums[i];
            if (idxMapper.contains(diff))
                return {idxMapper[diff], i};
            idxMapper[nums[i]] = i;
        }

        return res;
    }
};
