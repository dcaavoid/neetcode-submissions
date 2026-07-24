class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # x y x x y z b z b b i  s  l
        # 0 1 2 3 4 5 6 7 8 9 10 11 12
        #                     i
        # x: 3, y: 4, z: 7, b: 9, i: 10, s: 11, l: 12
        # end = 9
        # size = 5
        # res = [5, ]
        # Store the letter->lastIndex into a hash map.
        # Then iterate through the string s and update the end index.
        # If pointer i == end index, this is a valid substring.
        count = {}   #key=s[i], value=last index of s[i]
        for i, c in enumerate(s):
            count[c] = i
        
        res = []
        endIndex = 0
        size = 0
        for i in range(len(s)):
            lastIndex = count[s[i]]
            endIndex = max(endIndex, lastIndex)
            size += 1

            if i == endIndex:
                res.append(size)
                size = 0
                endIndex = 0

        return res