class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        drome = list(s)

        drome_copy = drome.copy()
        drome_copy.reverse()

        if drome == drome_copy:
            return True
        else:
            return False