# https://leetcode.com/problems/string-to-integer-atoi/description/

# Solved: 15/09/2024
# Runtime Beats: 65.03% (it's inconsistent)
# Memory Beats: 19.18%

class Solution:
    def myAtoi(self, s: str) -> int:
        output = ""
        output_sign = 1

        # Remove blank spaces from the beginning
        s = s.strip()
        for i, char in enumerate(s):

            # If the character is a number, add it
            if char in "0123456789":
                output += char

            # Stop when an alpha character is found
            if char.isalpha() or char == "." or char == " ":
                break

            # Deal with and "-" and "+" 
            if char == "-" or char == "+":
                if i > 0:
                    # Stop if the previous character was a number
                    if s[i-1] in "1234567890":
                        break

                if i < len(s)-1:
                    # If the next character is a number, make the result negative 
                    if s[i+1] in "1234567890":
                        if char == "-":
                            output_sign = -1
                    
                    # Otherwise, stop
                    else:
                        break
        
        # Deal with no output
        if output == "":
            output = 0
        
        # Convert to integer
        output = int(output)

        # Make negative if necessary
        output *= output_sign

        # Keep the number within bounds
        if output > pow(2, 31) - 1:
            output = pow(2, 31) - 1
        elif output < -1 * pow(2, 31):
            output = -1 * pow(2, 31)
        
        return output
