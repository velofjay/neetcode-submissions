class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return len(''.join(list(set(s))))
        res = 0
        for i in range(len(s)):
            charset = set()
            print(f"loop start charset {charset}")
            for j in range(i, len(s)):
                if s[j] in charset:
                    break
                charset.add(s[j])
            res = max(res, len(charset))
            print(f"after result charset {charset}")
        return res