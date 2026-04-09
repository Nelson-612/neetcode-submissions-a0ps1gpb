class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)
        if total % 2== 0:
            mid = total // 2
            return (merged[mid] + merged[mid-1]) / 2
        else:
            return float(merged[total // 2])