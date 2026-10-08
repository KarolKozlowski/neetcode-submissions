class Solution:
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz0123456789")

    def isPalindrome(self, s: str) -> bool:
        text = [char for char in s.lower() if char in self.allowed_characters]
        return text == text[::-1]  
        