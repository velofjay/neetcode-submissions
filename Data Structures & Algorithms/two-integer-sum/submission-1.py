class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce Time: O(n^2), Space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # now our goal is to convert that O(n^2) to O(n)
        # hashmap time: O(n), Space: O(n) (worst case scenario)
        other_half = {}
        for i in range(len(nums)):
            req = target - nums[i]
            
            if req in other_half:
                return [other_half[req], i]
            
            other_half[nums[i]] = i
        
        return []
             