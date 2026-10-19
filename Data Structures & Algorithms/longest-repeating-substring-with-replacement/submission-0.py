class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = defaultdict(int)
        l = 0
        maxlen = float('-inf')
        for r in range(len(s)):
            dict[s[r]] += 1
            maxfreq = max(dict.values())
            if (r-l+1)-maxfreq > k :
                dict[s[l]] -=1
                l += 1
            maxlen = max(maxlen,r-l+1)
        return maxlen
                    