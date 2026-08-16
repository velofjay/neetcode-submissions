class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        num_count_map = {}
        
        for num in nums:
            num_count_map[num] = nums.count(num)
        
        # sorting the dictionary bby values
        res = list(dict(sorted(num_count_map.items(), key=lambda x: x[1], reverse=True)[:k]).keys())
        
        return res
        # nums.count()
        # for num in nums:
            # if num == nums[indexof(num)+1]
            
        