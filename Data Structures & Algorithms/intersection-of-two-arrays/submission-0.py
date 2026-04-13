class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in result:
                        result.append(i)
        return result