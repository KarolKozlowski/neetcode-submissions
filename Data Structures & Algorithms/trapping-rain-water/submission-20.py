class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            move_left = left_max < right_max
            move_right = 1 - move_left

            left += move_left
            right -= move_right

            hl = height[left]
            hr = height[right]

            # Branchless max updates
            left_max = (left_max - hl) * (left_max > hl) + hl
            right_max = (right_max - hr) * (right_max > hr) + hr

            # Water calculation
            water += (left_max - hl) * move_left + (right_max - hr) * move_right

        return water