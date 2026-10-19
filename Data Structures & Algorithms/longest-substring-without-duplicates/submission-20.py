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
                if begin < seen[c] + 1:
                    begin = seen[c] + 1

            length = i - begin + 1
            max_len = max(length, max_len)
            seen[c] = i

            # print(seen)
            # print("max_len: {}, length: {}, begin: {}".format(max_len, length, begin))
        


        return max_len
