class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two i, j loops would still work but that will be O(n^2), hence lets proceed with prefix, suffix, res approach
        n = len(nums)
        prefix, suffix, result = [1] * n, [1] * n, [1] * n

        # create prefix array
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # create suffix array
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # product of final result
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result
        

        