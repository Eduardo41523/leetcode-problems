# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_solutions = []
        for i in range(len(nums)):
            current_number = nums[i]
            if(current_number in possible_solutions):
                return([i, possible_solutions.index(current_number)])
            possible_solutions.append(target - current_number)

