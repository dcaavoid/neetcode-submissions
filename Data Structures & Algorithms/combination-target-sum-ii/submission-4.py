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

            # [1, 2, 2, 3, 5, 6, 9]
            #  i  n
            # Recursive
            # 1. Choose current element
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # 2. not choose the current element, and skip any following elements that are the same as current element.
            nxt = i + 1
            while nxt < len(candidates) and candidates[nxt] == candidates[i]:
                nxt += 1
            
            curr.pop()
            dfs(nxt, total)
        
        dfs(0, 0)
        return res