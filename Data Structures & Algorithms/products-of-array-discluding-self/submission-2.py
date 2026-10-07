class Solution:
    def multiply(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            result *= num
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) > 1:
            # if there are at least two zeros all elements will be zero
            return [0] * len(nums)
        if nums.count(0) == 1:
            # if there is one zero, splice and multiply
            zero_at = nums.index(0)
            pre = nums[:zero_at]
            post = nums[zero_at+1:]
            product = self.multiply(pre + post)
            return [0] * len(pre) + [product] + [0] * len(post)
        else:
            # no zero
            output = []
            product = self.multiply(nums)
            for num in nums:
                output.append(int(product / num))
            return output