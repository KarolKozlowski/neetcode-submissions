from bisect import bisect_left, bisect_right

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums_s = sorted(nums)

        for i in range(len(nums_s) - 2):
            if i > 0 and nums_s[i] == nums_s[i - 1]:
                continue
            if nums_s[i] > 0:
                break

            j = i + 1
            k = len(nums_s) - 1

            while j < k:
                total = nums_s[i] + nums_s[j] + nums_s[k]

                if total < 0:
                    target = -nums_s[i] - nums_s[k]
                    j = bisect_left(nums_s, target, j + 1, k)
                elif total > 0:
                    target = -nums_s[i] - nums_s[j]
                    k = bisect_right(nums_s, target, j + 1, k) - 1
                else:
                    output.append([nums_s[i], nums_s[j], nums_s[k]])
                    j += 1
                    k -= 1

                    while j < k and nums_s[j] == nums_s[j - 1]:
                        j += 1
                    while j < k and nums_s[k] == nums_s[k + 1]:
                        k -= 1

        return output
