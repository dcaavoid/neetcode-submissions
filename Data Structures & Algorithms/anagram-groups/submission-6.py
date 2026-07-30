class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force: for each string of length n, sort each string, and use the sorted string as the key for a hash map.
        # Time: O(m * nlogn), space: O(m*n)
        # mapping = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     mapping[key].append(s)
        # return list(mapping.values())

        # Optimal solution: use an array of occurrence of each character as the key instead.
        # Optimize O(nlogn) to O(n) for each string
        mapping = defaultdict(list)   # [array of length 26]: [list of words with this occurrence]
        base = ord("a")
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - base] += 1
            mapping[tuple(key)].append(s)
        return list(mapping.values())