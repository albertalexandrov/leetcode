"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

"""


class Solution:
    def reverse(self, x: int) -> int:
        div, mod = divmod(abs(x), 10)
        result = mod
        while div:
            result *= 10
            div, mod = divmod(div, 10)
            result += mod
        if x < 0:
            result = -result
        return result if -2 ** 31 < result < 2 ** 31 - 1 else 0


solution = Solution()

assert solution.reverse(123) == 321
assert solution.reverse(-123) == -321
assert solution.reverse(120) == 21