import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Two versions:
        # Verion 1: min heap of size k: if size > k, pop smallest value.
        # Time: O(N*logK); space: O(K)
        # minHeap = []

        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        
        # return minHeap[0]

        # --------------------------------------------------------------------
        # Version 2: Quick select
        k = len(nums) - k

        def quickSelect(left: int, right: int):
            # Randomly choose a index as a pivot number
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot, p = nums[right], left

            # orig: [2, 3, 1, 5, 2, 6, 4], k = 2, pivot = 4
            # copy: [2, 3, 1, 2, 5, 6, 4]
            #                    p
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                return quickSelect(left, p - 1)
        
        return quickSelect(0, len(nums) - 1)
                