class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
      
        l = 0
        # while height[l] == 0: # skip sides
        #     l += 1

        r = len(height) - 1
        # while height[r] == 0: # skip sides
        #     l -= 1

        last_height = 0
        volume = 0

        while (l < r): 
            if height[l] < height[r]:
                volume += max(0, last_height - height[l])

                # volume -= min(height[l], last_height)
                last_height = max(height[l], last_height)

                # print("height[{}]: {}, height[{}]: {}, vol: {}".format(l, height[l], r, height[r], volume))
                l += 1
            else:
                volume += max(0, last_height - height[r])

                # volume -= min(height[r], last_height)
                last_height = max(height[r], last_height)

                # print("height[{}]: {}, height[{}]: {}, vol: {}".format(l, height[l], r, height[r], volume))
                r -= 1
        return volume
