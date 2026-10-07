class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     arr = []
    #     for num, count in count.items():
    #         arr.append([count, num])
        
    #     arr.sort()
        
    #     result = []
    #     while len(result) < k:
    #         result.append(arr.pop()[1])

    #     return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num, count in count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result