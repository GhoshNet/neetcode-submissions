class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr += char.lower()

        if newstr[::] == newstr[::-1]:
            return True
        else:
            return False