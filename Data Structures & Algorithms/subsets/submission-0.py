class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking with DFS
        # Not permutation, so different order of same elements count as one.
        res = []
        subset = []

        def dfs(i):
            # Base case: index out of bound.
            if i >= len(nums):
                # copy() snapshots the current subset;
                # Appending subset directly stores a reference that later append/pop mutations would corrupt.
                res.append(subset.copy())
                return
            
            # Recursive: either choose or not choose num at index i.
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res