class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums_s = sorted(nums)

        seen = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums_s[i] == -(nums_s[j] + nums_s[k]):
                    triplet = (nums_s[i], nums_s[j], nums_s[k])
                    if triplet not in seen:
                        seen.add(triplet)
                        output.append(list(triplet))
                    j += 1
                    k -= 1
                elif nums_s[i] < -(nums_s[j] + nums_s[k]):
                    j += 1
                elif nums_s[i] > -(nums_s[j] + nums_s[k]):
                    k -= 1
            if nums_s[i] > 0:
                break
 
        return output