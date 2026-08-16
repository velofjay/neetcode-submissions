import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_lower = s.lower()
        cleansed_str = re.sub(r'[^a-zA-Z0-9]', '', str_lower)
        return cleansed_str == cleansed_str[::-1]
        