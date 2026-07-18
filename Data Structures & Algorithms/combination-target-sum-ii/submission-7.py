class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS + sort
        # Since there are duplicate numbers and we want unique combinations, there are two choices for dfs:
        # 1. choose candidates[i] and do dfs(i+1)
        # 2. not choose candidates[i], skip all trailing numbers=candidates[i], and do dfs.
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            # Base case
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            # Recursive
            # 1. choose current number
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            # 2. skip all numbers = current number
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res