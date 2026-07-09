import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Two versions:
        # 1. Min heap with size k element.
        # Push into heap only if: (1) less than k elements; (2) top value is less than current value.
        # Time: O(n*log(k)); space(k)
        # minHeap = []

        # for num in nums:
        #     if len(minHeap) < k:
        #         heapq.heappush(minHeap, num)
        #     else:
        #         minNum = minHeap[0]
        #         if num > minNum:
        #             heapq.heappop(minHeap)
        #             heapq.heappush(minHeap, num)
        
        # return minHeap[0]
        
        # --------------------------------------------------------------------------------
        # 2. Quick Select to move pivot number to index len(nums) - k.
        # Every number of the left of pivot is less or equal to pivot;
        # Every number of the right of pivot is greater than pivot.
        # Use random pivot number from nums[left:right] each time to resolve the case where nums is sorted.

        def quickSelect(left, right):
            pivot_idx = random.randint(left, right)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            pivot, p = nums[right], left

            # Move any number less or equal to pivot to the left of pointer p.
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            # Move pivot number to pointer p.
            nums[right], nums[p] = nums[p], nums[right]

            # Check which partition does k in.
            if p == k:
                return nums[p]
            elif p > k:
                return quickSelect(left, p - 1)
            else:
                return quickSelect(p + 1, right)
        
        k = len(nums) - k
        return quickSelect(0, len(nums) - 1)