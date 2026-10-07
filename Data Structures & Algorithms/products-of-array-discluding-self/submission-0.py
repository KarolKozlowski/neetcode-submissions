import math
import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            temp = copy.copy(nums)
            temp.remove(num)
            prod = math.prod(temp)
            output.append(prod)
        return output