class Solution:
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz0123456789")

    def isPalindrome(self, s: str) -> bool:
        text = [char for char in s.lower() if char in self.allowed_characters]
        length = len(text)
        half = length // 2

        #  text[::-1][:half]

        return text[:half] == text[length-1:length-1-half:-1]
        