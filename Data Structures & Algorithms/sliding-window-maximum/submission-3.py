class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic decreasing queue that sort the number by its index.
        # Pop any smaller number first, and then add index of number to the end of deque,
        # once index > k, move left pointer by one,
        # 
        res = []
        deque = collections.deque()     # Index of number in nums
        left = 0

        for right in range(len(nums)):
            # Pop any smaller number before adding a new number.
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            
            deque.append(right)

            # Remove number that is out of bound
            if deque[0] < left:
                deque.popleft()
            
            # After the window is at least k, append max within the window
            if right + 1 >= k:
                res.append(nums[deque[0]])
                left += 1
        
        return res