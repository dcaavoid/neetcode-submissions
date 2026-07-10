class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Backtracking (DFS): For each number, two choices:
        # 1. 
        # Use an additional variable in dfs to track the remaining sum without calculating sum of an array each time.
        # How to ignore redundent combinations?
        # How to choose unlimited number of times?
        res = []
        curr = []

        def dfs(i, total):
            # Base case:
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # Recursive
            # 1. Choose the current number, keep the pointer at current index.
            curr.append(nums[i])
            dfs(i, total + nums[i])

            # Not choose the current number, move the pointer to the next index.
            curr.pop()
            dfs(i+1, total)
        
        dfs(0, 0)
        return res

