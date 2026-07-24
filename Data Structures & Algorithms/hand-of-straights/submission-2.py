class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Starting from the smallest number, try if num -> num + groupSize - 1 exist.
        # Use a hash map to track the occurence of each number.
        # Use min heap to retrieve the current smallest number in O(1).
        # Edge cases: 1. In [num, num + groupSize - 1], if num + i does not exist, return false;
        #             2. If we ever decrement the occurence to 0, but this number is not the start, we create a pit and return false;
        #             3. If len(hand) cannot be divisible by groupSize, return false.
        if len(hand) % groupSize:
            return False
        
        # key=hand[i], value=number of occurence of hand[i]
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True