class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Find the start of a sequence by checking whether (start - 1) exists.
        # Convert the input array into a hash set for O(1) retrival.
        numSet = set(nums)
        longest = 0
        
        for num in numSet:            
            # Find the start of a sequence
            if (num - 1) not in numSet:
                current = 0

                # Find if the next possible number exists
                while (num + current) in numSet:
                    current += 1
                
                longest = max(longest, current)
        
        return longest
