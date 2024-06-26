class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
    # Start from the last digit and add one
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
    
    # If all the digits were 9, the output should be '1' followed by all '0's
        return [1] + digits