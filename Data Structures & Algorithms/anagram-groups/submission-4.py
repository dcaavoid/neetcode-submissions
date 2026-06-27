class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # My attempt: Don't know what should i set as the key in the Hash Map
        # If we sort each string with average length of N,
        # the overall time complexity is O(M * Nlog(N)).
        # Instead, use an array of length 26 to count chars for each str
        # and use this as the key.
        
        # why defaultdict()? what does the parenthese define?
        res = defaultdict(list)    # key: array of 26, value: list of strings
        base = ord("a")

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - base] += 1
            
            # Since list cannot be keys in Hash Map, turn into tuple
            # b/c tuple is non-mutable.
            res[tuple(count)].append(s)
        
        return list(res.values())