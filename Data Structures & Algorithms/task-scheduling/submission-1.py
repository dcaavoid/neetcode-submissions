class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the number for each task;
        # Sort the task by the frequency in descending order (max heap);
        # After finishing the most frequent task, save the (freq - 1, time + n) pair for next visit.
        maxHeap = []
        mapping = {}
        q = collections.deque()   # (- number of task, time): for next visit

        # Count the number of each task.
        for t in tasks:
            if t not in mapping:
                mapping[t] = 0
            mapping[t] += 1
        
        # Push the number of tasks into max heap for O(1) retrival.
        for val in mapping.values():
            heapq.heappush(maxHeap, -1 * val)
        
        time = 0
        while maxHeap or q:
            time += 1
            # If there are available tasks without idle.
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                # Add tasks to queue if remaining
                if freq:
                    q.append((freq, time + n))
            
            # Check if a task has reached idle time.
            if q and q[0][1] == time:
                freq, _ = q.popleft()
                heapq.heappush(maxHeap, freq)
        
        return time