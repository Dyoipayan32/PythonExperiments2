class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1 + nums2
        nums1.sort()
        zeros = nums1.count(0)
        nums1 = nums1[(zeros):]

