class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()   # Set of indices in target that found matching in triplets.

        for t in triplets:
            # Skip triplets with larger value than target at any indices.
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Find if each target number has a match in any triplets.
            for idx, val in enumerate(t):
                if val == target[idx]:
                    valid.add(idx)
        
        return len(valid) == 3
        