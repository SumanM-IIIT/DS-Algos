# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
# non-negative integers and empty spaces .

# Example 1:
# Input: "1 + 1"
# Output: 2

# Example 2:
# Input: " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution:
    def calculate(self, s: str) -> int:
        num, res, sign = 0, 0, 1
        stack = []

        for char in s:
            if char in '1234567890':
                num = 10*num + int(char)
            elif char in '+-':
                res += sign*num
                if char == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ')':
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + sign*num
