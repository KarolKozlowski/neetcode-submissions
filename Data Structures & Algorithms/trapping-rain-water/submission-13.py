class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
      
        l = 0
        while height[l] == 0: # skip sides
            print("height[{}]: {}".format(l, height[l]))
            l += 1

        r = len(height) - 1
        while height[r] == 0: # skip sides
            print("height[{}]: {}".format(r, height[r]))
            r -= 1

        if l == r:
            return 0

        last_height = 0
        volume = 0

        while (l < r): 
            if height[l] < height[r]:
                if height[l] < last_height:
                    volume += last_height - height[l]
                else:
                    last_height = height[l]
                l += 1

            else:
                if height[r] < last_height:
                    volume += last_height - height[r]
                else:
                    last_height = height[r]
                r -= 1

        return volume
