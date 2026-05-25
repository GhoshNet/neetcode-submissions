import numpy as np

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        cap = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height 
            cap = max(area, cap)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return cap