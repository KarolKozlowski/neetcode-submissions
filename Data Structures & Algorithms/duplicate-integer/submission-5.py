class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#         temp = set()
#         for i in range(0,len(nums)):
#             if nums[i] in nums[i+1:]:
#                 return True
#         return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False