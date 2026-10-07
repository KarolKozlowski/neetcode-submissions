class Solution:
    separator = "\x00"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.separator
        else:
            encoded = self.separator.join(strs)
            return self.separator + encoded + self.separator

    def decode(self, s: str) -> List[str]:
        if s == self.separator:
            return []
        else:
            decoded = s.split(self.separator)
            return decoded[1:len(decoded)-1]
