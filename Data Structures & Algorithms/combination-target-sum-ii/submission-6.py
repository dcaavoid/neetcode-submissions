class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking with DFS.
        # Different from Leetcode 39 b/c in Leetcode 39, each number is distinct.
        # In DFS, two choices:
        # 1. choose the current element, and go to next elements;
        # 2. not choose the current element and skip any following duplicate elements.
        # So need to sort the array first.
        candidates.sort()
        res = []
        curr = []

        def dfs(i, total):
            # Base case
            if total == target:
                res.append(curr.copy())
                return
            
            if i == len(candidates) or total > target:
                return

            # Recursive
            # 1. Choose candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # 2. Skip candidates[i] and any following candidates[i + 1] == candidates[i]
            curr.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            
            dfs(i + 1, total) # Don't understand why we i + 1 here as we update i?
         
        dfs(0, 0)
        return res