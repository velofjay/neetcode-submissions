class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        three_sum_list.append(sorted([nums[i], nums[j], nums[k]]))
        unique = list({tuple(elem) for elem in three_sum_list})
        return unique