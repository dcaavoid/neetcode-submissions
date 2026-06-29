class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic decreasing deque: track the index of nums b/c we need to check if the current max is out of bound of k.
        # [8, 7, 6, 9], k = 3
        # q = [8, 7, 6]
        
        q = collections.deque()   # Index of nums
        res = []
        l = r = 0

        while r < len(nums):
            # Before adding num, remove any num in deque that is smaller than the current num
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove number that is out of bound
            if l > q[0]:
                q.popleft()

            # Only add current max to the result list if the window is big enough
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
