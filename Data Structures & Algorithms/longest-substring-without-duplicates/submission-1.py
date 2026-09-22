class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = defaultdict(int)
        l,maxlen = 0,0
        for r in range(len(s)):
            if s[r] in dict and dict[s[r]]>=l:
                l = dict[s[r]] + 1
            dict[s[r]] = r
            maxlen = max(maxlen,r-l+1)
        return maxlen
