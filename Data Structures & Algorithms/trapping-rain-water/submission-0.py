class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        cap = 0
        
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                cap += leftMax - height[left]
            
            elif rightMax <= leftMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                cap += rightMax - height[right]

        return cap