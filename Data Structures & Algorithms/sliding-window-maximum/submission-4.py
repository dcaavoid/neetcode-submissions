class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Sliding window + monotonic queue (decreasing)
        q = collections.deque()     # index in nums
        res = []
        left = 0
        for right in range(len(nums)):
            # First pop number that is out of bound
            # Pop once b/c we add at most one num to the queue at a time.
            if q and q[0] < left:
                q.popleft()
            
            # Pop all smaller nums from the end of queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if right + 1 >= k:
                left += 1
                res.append(nums[q[0]])
        
        return res