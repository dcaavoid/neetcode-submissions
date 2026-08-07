class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [4, 1, 0, 7], target = 10, speed = [2, 2, 1, 1]
        # [(0, 3), (1, 1), (4, 0), (7, 3)]
        # (10 - 7) / 1 = 3
        # (10 - 4) / 2 = 3
        # (10 - 1) / 2 = 5
        # (10 - 0) / 1 = 10

        # Earlier car depends on later car -> sort by position in decreasing order
        stack = []   # store group of time to reach destination
        pairs = sorted(zip(position, speed), reverse=True)
        for p, s in pairs:
            t = (target - p) / s
            
            # Check if there is slower cars in the front
            if not stack or stack[-1] < t:
                stack.append(t)
        
        return len(stack)
