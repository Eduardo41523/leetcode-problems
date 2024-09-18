# https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18

# Solved: 18/09/2024
# Runtime Beats: 5.31%%
# Memory Beats: 32.99%

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def secondNumberBetterFirst(a, b):
            return int(str(a) + str(b)) < int(str(b) + str(a))

        # I used bubble sort for my first answer, as it's the sorting algorithm I know best atm
        # A better sorting algorithm would undoubtedly give better results
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if secondNumberBetterFirst(nums[j], nums[j+1]):
                    bucket = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = bucket

        output = "".join(str(num) for num in nums)

        return str(int(output))