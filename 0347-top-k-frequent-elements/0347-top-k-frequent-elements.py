class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        countMap = {}

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
            
        for num, freq in countMap.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        return [num for freq, num in heap]