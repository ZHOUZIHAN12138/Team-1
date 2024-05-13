# Plus One Solution

## Description
This repository contains a Python solution for the "Plus One" problem, where you're given a non-empty array of decimal digits representing a non-negative integer. The digits are stored such that the most significant digit is at the head of the list. This implementation provides a method to increment this integer by one.

## Implementation
The `Solution` class includes the method `plusOne`, which takes a list of integers as input and returns a list of integers representing the incremented value.

### Method: plusOne
The `plusOne` method starts by checking from the last digit of the array and adds one to it. If the digit is less than 9, it is incremented, and the array is returned immediately. If the digit is 9, it turns into 0, and the method continues to the next significant digit to handle the carryover. If all digits are 9, the array is expanded to accommodate the new significant digit due to carryover.

#### Parameters:
- `digits` (List[int]): A list of integers where each integer is a single decimal digit.

#### Returns:
- List[int]: A list of integers representing the integer after incrementing by one.

## Example Usage
```python
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
