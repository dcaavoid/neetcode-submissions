class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use max heap (get the most occurence letter) + queue (track next available letter after certain idle).
        count = Counter(tasks)    # Hash map: key -> number of occurence.
        maxHeap = [-c for c in count.values()]    # Max heap that only stores the occurence.
        heapq.heapify(maxHeap)
        queue = deque()   # Store (-count, time + idle)
        time = 0

        while maxHeap or queue:
            time += 1

            # If there is available tasks to execute next:
            if maxHeap:
                # Since -count in max heap, 1 + (-count) decrease the occurence by one.
                curr = 1 + heapq.heappop(maxHeap)

                # If curr is not 0, add the next available time to visit to the queue.
                if curr:
                    queue.append((curr, time + n))

            # If there is task that reacht he idle time
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time