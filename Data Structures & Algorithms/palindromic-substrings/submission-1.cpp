class Solution {
public:
    int countSubstrings(string s) {
        int len = s.length();
        int res = len;
        for (int i=0; i<len; i++)
        {
            int even = expand(i, i, s);
            int odd = expand(i, i+1, s);
            // std::cout<<(even);
            // std::cout<<(odd);
            res += even + odd;
            // std::cout<<(res);
        }
        return res;
    }

    int expand(int left, int right, string s)
    {
        int count = 0;
        if (left == right) //'a'
            count  -= 1;
        while (left >= 0 && right < s.length() && s[left] == s[right])
        {
            // std::cout<<s[left];
            // std::cout<<s[right];
            count += 1;
            left -= 1;
            right += 1;
        }
        return count;
    }
};
