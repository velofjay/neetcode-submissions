class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = {}

        # creates num and its occurrences freq hashmap
        for num in nums:
            freq_num[num] = freq_num.get(num, 0) + 1

        # convert the dict to list of tuples(as these are ordered mutable collection) {1:1, 2:2, 3:3} -> [(1,1), (2,2), (3,3)]
        freq_num_list = list(freq_num.items())

        # sort based on highest freq
        freq_num_list.sort(key=lambda x: x[1], reverse=True) # until that lambda x[1] we will have ascending order sorted based on freq, and we used reverse to make it descending order - which is highest freq comes first [()]

        # run loop on first k and return the list
        res = []
        for i in range(k):
            res.append(freq_num_list[i][0])
        return res
