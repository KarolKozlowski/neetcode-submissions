class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = str()
        for string in strs:
            encoded_str += str(len(string))
            encoded_str += "#"
            encoded_str += string
        # print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        last_marker = -1
        output = []
        index = 0
        # for index in range(0,len(s)):
        while index < len(s):
            if s[index] == "#":
                # print(s[last_marker + 1:index])
                length = int(s[last_marker + 1:index])
                output.append(s[index + 1:index + 1 + length])
                last_marker = index + length
                index += length + 1
            else:
                index += 1

        return output
