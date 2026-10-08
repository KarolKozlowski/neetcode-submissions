class Solution:
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz0123456789")

    def isPalindrome(self, s: str) -> bool:
        text = [char for char in s.lower() if char in self.allowed_characters]
        text_lenght = len(text)

        for i in range(int(text_lenght/2)):
            if text[i] != text[text_lenght - 1 - i]:
                return False

        return True
        