import re

class Solution:
    allowed_characters = r"[^a-zA-Z0-9]+"
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(self.allowed_characters, "", s).lower()
        text_lenght = len(text)

        for i in range(int(text_lenght/2)):
            if text[i] != text[text_lenght - 1 - i]:
                return False

        return True
        