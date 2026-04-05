class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        i, j = 0, len(height) - 1
        maxLeft = height[i]
        maxRight = height[j]
        water = 0

        while i < j:
            if maxLeft < maxRight:
                i += 1
                maxLeft = max(maxLeft, height[i])
                water += maxLeft - height[i]
            else:
                j -= 1
                maxRight = max(maxRight, height[j])
                water += maxRight - height[j]
        return water
