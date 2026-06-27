class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a to z
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s) # dictionary keys must be immutable and hashable
        return list(result.values())
