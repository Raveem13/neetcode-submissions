class Solution:
    def isPalindrome(self, s: str) -> bool:
        shortString = ""
        for c in s:
            if c.isalnum():
                shortString += c.lower() 
        return shortString == shortString[::-1]