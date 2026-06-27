class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Intuitive: hash table, and then sort the value, and then return top k
        # Bucket sort: create a array of length len(nums) b/c in the worst case,
        # all numbers in nums are the same.
        # Array for bucket sort: index=count of number, value=list of number with that count
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []

        # Count the occurence of each value
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Iterate through each number and add to the corresponding bucket
        for n, c in count.items():
            bucket[c].append(n)
        
        # Return top k from the end of the bucket array
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                k -= 1

                if k == 0:
                    return res
            
            