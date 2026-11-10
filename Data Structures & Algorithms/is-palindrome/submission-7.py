class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        print(s)
        for char in s:
            if 65 <= ord(char) <= 90 or 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                continue
            else:
                s = s.replace(char, "")
        
        s = s.lower()
        return s == s[::-1]