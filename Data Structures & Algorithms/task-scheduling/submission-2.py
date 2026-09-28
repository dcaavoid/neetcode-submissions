class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a global time to track
        # Create a queue (-freq, available time) to track next available task
        time = 0
        maxHeap = []    # (-freq)
        queue = collections.deque()     # (-freq, time)
        taskToFreq = {}   # task: freq

        # Create a hashMap to track the freq of each task
        for t in tasks:
            if t not in taskToFreq:
                taskToFreq[t] = 0
            taskToFreq[t] += 1
        
        # Create a maxHeap (-freq) to track most freq available task
        for val in taskToFreq.values():
            heapq.heappush(maxHeap, -1 * val)
        
        while maxHeap or queue:
            time += 1

            # Process the task with most freq first
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)   # decrement by one
                if freq:
                    queue.append((freq, time + n))
            
            # If there is available task in queue
            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(maxHeap, freq)
        
        return time
            