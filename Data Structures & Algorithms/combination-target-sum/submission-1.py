class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # DFS with two choices:
        # 1. choose the current number and continue dfs; 
        # 2. not choose the current number and continue dfs from the next number.
        # Since all numbers are distinct, no need to think about duplicates.
        res = []

        # [2, 5, 6, 9]
        #  i

        def dfs(i: int, prevSum: int, curr: List[int]):
            # Base case
            if prevSum == target:
                res.append(curr.copy())
                return
            if prevSum > target or i == len(nums):
                return
            
            # Recursive
            curr.append(nums[i])
            dfs(i, prevSum + nums[i], curr)
            curr.pop()
            dfs(i + 1, prevSum, curr)
        
        dfs(0, 0, [])
        return res
            
            