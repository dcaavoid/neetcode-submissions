class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if there are only two numbers in the array
        if(len(nums) == 2):
            return [0, 1]
        
        # general
        hashMap = {} # val -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i