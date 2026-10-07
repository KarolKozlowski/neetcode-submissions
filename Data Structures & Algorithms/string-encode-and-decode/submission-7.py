class Solution:
    separator = "\x00"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return self.separator + self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s[1:].split(self.separator)