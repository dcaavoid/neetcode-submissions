class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for n, c in freq.items():
            count[c].append(n)
        
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)

                if len(res) == k:
                    return res