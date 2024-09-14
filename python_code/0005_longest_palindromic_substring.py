# https://leetcode.com/problems/longest-palindromic-substring/description/

# Solved: 13/09/2024
# Runtime Beats: 46.90%
# Memory Beats: 19.45%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome_length_record = 1
        index_of_record = 0

        # Loop over every single letter of the string, except the last
        for i in range(len(s)-1):
            # Checking if s[i] is at the absolute centre of an odd length palindrome
            palindrome_length = 1
            j = 1
            while i-j >= 0 and i+j <= (len(s)-1):
                if s[i-j] == s[i+j]:
                    palindrome_length += 2
                    if palindrome_length > palindrome_length_record:
                        palindrome_length_record = palindrome_length
                        index_of_record = i-j
                else:
                    break
                j += 1

            # Checking if s[i] is at the left centre of an even length palindrome
            palindrome_length = 0        
            j = 0
            while i-j >= 0 and i+1+j <= (len(s)-1):
                if s[i-j] == s[i+1+j]:
                    palindrome_length += 2
                    if palindrome_length > palindrome_length_record:
                        palindrome_length_record = palindrome_length
                        index_of_record = i-j
                else:
                    break
                j += 1


        longest_palindrome = s[index_of_record:index_of_record + palindrome_length_record] 

        return longest_palindrome