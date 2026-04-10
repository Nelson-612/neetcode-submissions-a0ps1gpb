class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            maxArea = max(maxArea, (right-left)*min(heights[left], heights[right]))
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return maxArea