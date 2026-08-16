class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # for mapping

        for s in strs:
            sorted_form_of_s = ''.join(sorted(s))
            res[sorted_form_of_s].append(s)
        return list(res.values())