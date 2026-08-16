class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''proceeding with hashset so that we can have: 
        Time complexity as O(n) and 
        space complexity as O(n)'''
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False