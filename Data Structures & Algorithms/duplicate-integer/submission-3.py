class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use Set
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        
        return False