class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = -1
        # minLen = -1
        for word in wordDict:
            maxLen = max(maxLen, len(word))
            # minLen = min(minLen, len(word))
        # stack = [-1] *len(s)
        visited = set()
        visited.add(-1)

        for end in range(len(s)):
            for word in wordDict:
                # print(end,word)
                endIdx = end+len(word)-1
                newStr = s[end: end+len(word)]

                if end-1 not in visited:
                    continue
                if endIdx >= len(s):
                    continue
                if newStr == word:
                    # print(endIdx)
                    if endIdx == len(s)-1:
                        return True
                    visited.add(endIdx)

        return False

        

            