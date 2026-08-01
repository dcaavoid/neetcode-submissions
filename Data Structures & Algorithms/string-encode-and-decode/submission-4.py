class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode word by length of string + # as the separator.
        # This works even though # might be in the actual string b/c we don't need to search inside the actual string.
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"

            for c in s:
                res += c
        
        return res

    def decode(self, s: str) -> List[str]:
        # 3#abc4#cdef
        res = []
        i = 0
        while i < len(s):
            # Get the length of each word and convert into integer.
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # Save decoded string
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return res