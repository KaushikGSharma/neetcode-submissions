class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        import heapq
        from collections import defaultdict
        from collections import Counter

        freq = Counter(tasks)

        mp=dict(sorted(freq.items(), key=lambda i:i[1], reverse=True))
        print(mp)
        queue=deque()
        heap=[]
        result=0
        for key,value in mp.items():
            heapq.heappush(heap,(-value,key))
        
        while len(heap)>0 or len(queue)>0:
            result+=1
            if len(heap)>0:
                value,key= heapq.heappop(heap)
                value+=1
                if value<0:
                    queue.append((value,key, result+n))
            
            if queue and queue[0][2] <= result:
                val, key, _ = queue.popleft()
                heapq.heappush(heap,(val,key))
            
        
        return result
            






