class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force: for each string of length n, sort each string, and use the sorted string as the key for a hash map.
        # Time: O(m * nlogn), space: O(m*n)
        mapping = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            mapping[key].append(s)
        return list(mapping.values())