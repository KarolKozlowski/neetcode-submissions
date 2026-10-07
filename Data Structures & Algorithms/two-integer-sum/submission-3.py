class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1


        for i in range(len((nums))):
            for j in reversed(range(len((nums)))):
                if j == i:
                    continue
                # print("i={}, j={}, sum={}, target={}".format(i, j, nums[i] + nums[j], target))
                if nums[i] + nums[j] == target:
                    return [i, j]

        