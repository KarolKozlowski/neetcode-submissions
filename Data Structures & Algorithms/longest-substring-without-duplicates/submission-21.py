class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = {}

        max_len = 0
        begin = 0

        for i in range(len(s)):
            c = s[i]

            if c in seen:
                begin = max(begin, seen[c] + 1)

            length = i - begin + 1
            max_len = max(length, max_len)
            seen[c] = i

        return max_len
