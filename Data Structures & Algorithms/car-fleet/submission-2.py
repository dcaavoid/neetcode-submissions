class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Stack to track the time of arriving the destination.
        # Sort by the position first, and then calcuate arrival time starting from the end.
        # This is b/c for any car that is faster at the back, they will merge into one fleet and keep the slower speed.
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(key=lambda x: x[0])

        for i in range(len(pair) - 1, -1, -1):
            p, s = pair[i]
            time = (target - p) / s

            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)