class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = {}

        begin = 0
        max_len = 0

        # print("len(s): {}".format(len(s)))

        for i in range(len(s)):
            c = s[i]

            # print("i: {}, {} - {} - {}, seen: {}".format(i, s[:i], s[i], s[i:], seen))
            # print(" {} in seen: {}".format(c, c in seen))
            
            if c in seen:
                # print("begin < seen[c]: {} < {}: {}".format(begin, seen[c], begin < seen[c]))
                new_begin = seen[c] + 1;

                while begin < new_begin:
                    # print("c: {}, begin: {}, s[begin]: {}, seen[c]: {}".format(c, begin, s[begin], seen[c]))
                    seen.pop(s[begin])
                    begin += 1
                seen[c] = i

            else:
                seen[c] = i
                # print("len(seen): {}, max_len: {}".format(len(seen), max_len))
                max_len = max(len(seen), max_len)
        
        return max_len
