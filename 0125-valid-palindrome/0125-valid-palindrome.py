class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpace = ""
        for char in s:
            if char.isalnum():
                noSpace += char.lower()
        return noSpace == noSpace[::-1]
        