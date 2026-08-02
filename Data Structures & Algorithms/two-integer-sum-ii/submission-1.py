class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers (left and right)
        # Update two pointers based on the relationship between sum and target.
        # Time: O(n) as each number is visited at most once; space: O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1