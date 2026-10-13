class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_vol = 0

        while (l < r):
            volume = (r-l) * min(heights[l], heights[r])
            if volume > max_vol:
                max_vol = volume 
            # print("h[{}]:{}, h[{}]: {}, v={}".format(l, heights[l], r, heights[r], volume))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol