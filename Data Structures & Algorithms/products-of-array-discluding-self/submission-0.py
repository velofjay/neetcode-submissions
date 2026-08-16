class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # op_prod = []
        # for num in nums:
        length = len(nums)
        res = [0] * length
        
        for i in range(length):
            prod = 1
            for j in range(length):
                if i == j:
                    continue
                prod *= nums[j]
            
            res[i] = prod
        
        return res
            
        