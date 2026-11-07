class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ''
        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right- left + 1) - 2 #increase before leaving while loop
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            currLen =  max(odd,even)
            if currLen > maxLen:
                maxLen = currLen
                start = i - (currLen - 1) // 2

        return s[start:start + maxLen]
        