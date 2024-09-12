# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Solved: 12/09/2024
# Runtime Beats: 84.20%
# Memory Beats: 40.60%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        current_streak = 0
        current_group = []
        for char in s:
            if (char not in current_group):
                current_streak += 1
                current_group.append(char)

                if current_streak > longest_substring_length:
                    longest_substring_length = current_streak
            else:
                current_streak -= current_group.index(char) + 1
                current_group = current_group[1:]

        return longest_substring_length


