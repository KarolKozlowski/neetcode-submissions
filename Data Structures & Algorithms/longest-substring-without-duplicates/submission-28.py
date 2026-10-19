class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = {}

        max_len = 0
        begin = 0

        # for i in range(len(s)):
        #     c = s[i]

        for i, c in enumerate(s):
            begin = max(begin, seen.get(c, -1) + 1)

            max_len = max(max_len, i - begin + 1)
            seen[c] = i

        return max_len
