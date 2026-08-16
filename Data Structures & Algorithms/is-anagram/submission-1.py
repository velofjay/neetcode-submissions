class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s, cnt_t = {}, {}

        for i in range(len(s)):
            cnt_s[s[i]] = cnt_s.get(s[i], 0) + 1
            cnt_t[t[i]] = cnt_t.get(t[i], 0) + 1
        
        for elem in cnt_s:
            if cnt_s[elem] != cnt_t.get(elem, 0):
                return False
        return True
        