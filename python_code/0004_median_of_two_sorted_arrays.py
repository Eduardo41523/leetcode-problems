# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Solved: 12/09/2024
# Runtime Beats: 19.26%
# Memory Beats: 64.57%

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()

        middle_index = len(merged_array)//2
        print(middle_index)
        if len(merged_array) % 2 == 0:
            return (merged_array[middle_index] + merged_array[middle_index-1])/2
        elif len(merged_array) % 2 == 1:
            return merged_array[middle_index]