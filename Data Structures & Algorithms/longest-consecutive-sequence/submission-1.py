class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num hashset
        num_hashset = set(nums)

        # long init
        longest = 0

        # loop through the set
        for num in num_hashset:
            # see if this is start of seq
            if (num - 1) not in num_hashset:
                current = num
                length = 1

                while (current + 1) in num_hashset:
                    current += 1
                    length += 1

                longest = max(longest, length)
            
        return longest

        

        