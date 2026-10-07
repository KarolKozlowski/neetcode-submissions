class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}

        for i in nums:
            if i in buckets:
                buckets[i] = buckets[i] + 1
            else:
                buckets[i] = 1

        return sorted(buckets, key=buckets.get, reverse=True)[0:k]