class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal: create an array of size n + 1, and ith index represents the number with number of i frerequenies.
        freq = {}   # number: frequency
        count = [ [] for _ in range(len(nums) + 1) ]
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for n, f in freq.items():
            count[f].append(n)
        
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
            
            if len(res) == k:
                return res

        # Brute force: create a hash map (number: freq) for nums, sort based on the frequency and select top k.
        # Time: O(n log n)
        # count = {}
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        
        # pairs = list(count.items())
        # pairs.sort(key=lambda x: x[1], reverse=True)    # Sort by the value (freq) in reverse order
        # return [num for num, freq in pairs[:k]]