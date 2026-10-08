class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # speed up lookups
        nums_set = set(nums)

        beginnings = []

        for num in nums:
            if num - 1 not in nums_set:
                beginnings.append(num)
        
        max_len = 0
        for num in beginnings:
            i = 0
            while num + i in nums_set:
                i += 1
                if max_len < i:
                    max_len = i

        return max_len
            



                


        