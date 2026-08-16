class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        num_set = set(nums)

        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                curr = n
                length = 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                longest = max(longest, length)
            
        return longest
            # for i in range(len(asc_list)):
            #     if asc_list[i+1] - asc_list[i] == 1:
            #         count += 1
            #         print(count)
            # return count
        