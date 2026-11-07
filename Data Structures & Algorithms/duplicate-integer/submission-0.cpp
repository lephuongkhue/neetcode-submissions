class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> visited;
        for(int n: nums)
        {
            if (visited.contains(n))
                return true;
            visited.insert(n);
        }
        return false;
    }
};