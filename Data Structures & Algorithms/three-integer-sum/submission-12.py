class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums_s = sorted(nums)

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print("num[{}]: {}, num[{}]: {}, num[{}]: {}, sum: {}".format(i, nums_s[i], j, nums_s[j], k, nums_s[k], nums_s[i]+nums_s[j]+nums_s[k]))
                if nums_s[i] == -(nums_s[j] + nums_s[k]):
                    triplet = ([nums_s[i], nums_s[j], nums_s[k]])
                    if triplet not in output:
                        output.append(triplet)
                    j += 1
                    k -= 1
                elif nums_s[i] < -(nums_s[j] + nums_s[k]):
                    j += 1
                elif nums_s[i] > -(nums_s[j] + nums_s[k]):
                    k -= 1
 
        return output