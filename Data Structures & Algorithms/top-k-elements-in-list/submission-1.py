from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=defaultdict(int)
        result=[]
        heap=[]

        for i in nums:
            mp[i]=mp[i]+1
        print(mp)

        for key,value in mp.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)

        for value,key in heap:
            result.append(key)
        
        return result