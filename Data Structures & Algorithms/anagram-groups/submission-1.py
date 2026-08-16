class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap sorted ones as a key
        anagrams_map = {}
        for elem in strs:
            sorted_key = ''.join(sorted(elem))
            if sorted_key in anagrams_map:
                anagrams_map[sorted_key].append(elem)
            else:
                anagrams_map[sorted_key] = [elem]
        return list(anagrams_map.values())