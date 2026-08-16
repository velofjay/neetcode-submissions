class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = ""
        encoded_list = []
        for elem in strs:
            encoded_list.append(f'{len(elem)}#{elem}')
        encoded_string = sep.join(encoded_list)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # find '#'
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            j += 1

            # now lets extract actual string
            string = s[j:j+length]
            res.append(string)

            # move pointer to the next block
            i = j + length
        # sep = "$JV$"
        # decoded_string = s.split(sep)
        return res
